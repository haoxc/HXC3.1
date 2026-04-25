# UML 类图（Obsidian / PlantUML）

> 用法：在 Obsidian 中启用 PlantUML 插件后，直接打开本文件，或复制任一 `plantuml` 代码块到笔记中即可渲染。
>
> 说明：仓库是多模块 Java/Eclipse 插件工程，类数量较多。这里按“领域模型 -> 调度决策 -> RCPSP 扩展 -> 策略运行时 -> 工具视图”的层次做了精简类图，保留主干接口、实现类和关键聚合关系。

## 1. 全局模块关系

```plantuml
@startuml
left to right direction
skinparam classAttributeIconSize 0

class Core <<module>> {
  +problemContracts
  +dataProvider
  +objective
}

class ECRuntime <<module>> {
  +strategyRuntime
  +population
  +operators
}

class FJSPModel <<module>> {
  +manufactureModel
  +decisionModel
}

class RCPSP <<module>> {
  +projectScheduling
  +uncertaintyModel
}

class SA <<module>> {
  +simulatedAnnealing
}

class FJSPAdapter <<module>> {
  +dataLoader
  +objective
  +chartProvider
}

class PolicyTree <<module>> {
  +policyTreeModel
  +zestView
}

class DiagramUI <<module>> {
  +graphViewer
  +umlFigures
}

ECRuntime ..> Core : base contracts
FJSPModel ..> Core : IProblemSolution
SA ..> ECRuntime : strategy runtime
RCPSP ..> FJSPModel : extends scheduling model
FJSPAdapter ..> FJSPModel : adapts problem data
FJSPAdapter ..> Core : data contracts
PolicyTree ..> DiagramUI : visualization support
@enduml
```

## 2. FJSP 领域模型

```plantuml
@startuml
left to right direction
skinparam classAttributeIconSize 0

interface Identifying {
  +getInternalId() : int
  +getId() : int
  +getName() : String
  +getIndex() : int
}

interface ManufactureFactory {
  +getId() : int
  +getName() : String
  +getProducts() : List<Product>
  +getMachineManger() : MachineManager
  +getResourceManger() : ResourceManager
  +getProblemId() : String
  +getBenchmark() : String
  +getProduct(index) : Product
}

interface FJSPModel

interface Product {
  +getCatagory() : ProductCategory
  +getOperations() : List<Operation>
  +getRootOperations() : List<Operation>
  +createOperation() : Operation
  +link(curOperationId, successorId) : void
  +notation() : String
}

interface Operation {
  +getProduct() : Product
  +getSuccessor() : List<Operation>
  +getPredecessor() : List<Operation>
  +getConfigurations() : List<MachiningConfiguration>
  +isDummy() : boolean
  +isRoot() : boolean
  +addSuccessor(successor) : void
  +randomConfiguration() : MachiningConfiguration
}

interface MachiningConfiguration {
  +getOperation() : Operation
  +getMachine() : Machine
  +getProcessingTime() : double
  +getRelationship() : RelationType
  +getResources() : List<ResourceConstrain>
  +getMachineId() : int
}

interface AbstractResource {
  +getCapacity() : long
  +getFixCost() : double
  +getProcessingCost() : long
}

interface Machine {
  +getItems() : List<MachineItem>
  +getConstrains() : MachiningConfiguration
  +isVirtual() : boolean
  +hasSameTypeWith(target) : boolean
  +notation() : String
}

interface Resource {
  +getCategory() : ResourceCategory
  +getItems() : List<ResourceItem>
  +getResourceTypeId() : int
}

interface ProductCategory

interface ResourceCategory {
  +getResources() : List<Resource>
  +addResource(capacity) : Resource
  +getResource(resourceId) : Resource
}

interface MachineManager {
  +getMachines() : List<Machine>
  +getById(machineId) : Machine
  +getByIndex(index) : Machine
  +createMachine(capacity) : Machine
}

interface ResourceManager {
  +getResourceTypes() : List<ResourceCategory>
  +createResourceType(typeId, typeName) : ResourceCategory
  +createConfiguration(resourceIds) : MachiningConfiguration
  +getResourceByInternalId(internalResourceId) : Resource
}

interface ResourceConstrain
enum RelationType

ManufactureFactory <|-- FJSPModel
Identifying <|-- Product
Identifying <|-- Operation
Identifying <|-- MachiningConfiguration
Identifying <|-- AbstractResource
Identifying <|-- ProductCategory
Identifying <|-- ResourceCategory
AbstractResource <|-- Machine
AbstractResource <|-- Resource

ManufactureFactory "1" *-- "0..*" Product : products
ManufactureFactory "1" *-- "1" MachineManager : machine manager
ManufactureFactory "1" *-- "1" ResourceManager : resource manager
MachineManager "1" *-- "0..*" Machine : machines
ResourceManager "1" *-- "0..*" ResourceCategory : resource types
ResourceCategory "1" *-- "0..*" Resource : resources
Product "1" *-- "0..*" Operation : operations
Product --> ProductCategory : category
Operation "1" *-- "0..*" MachiningConfiguration : configurations
Operation --> "0..*" Operation : successor
Operation --> "0..*" Operation : predecessor
MachiningConfiguration --> Machine : machine
MachiningConfiguration --> RelationType : relationship
MachiningConfiguration --> "0..*" ResourceConstrain : resources
Machine --> MachiningConfiguration : constrains
@enduml
```

## 3. FJSP 调度决策模型

```plantuml
@startuml
left to right direction
skinparam classAttributeIconSize 0

interface IProblemSolution

interface IFJSP2Solution {
  +create(context, cloneDecision) : void
  +getCompleteTime() : double
  +setModel(model) : void
  +getProductDecisions() : List<ProductDecision>
  +getMachineDecision() : List<MachineDecision>
  +getResourceDecisions() : List<ResourceStorageDecision>
  +getOpSequence() : List<OperationDecision>
  +getCriticalPath() : CriticalPath
  +leftShift() : boolean
  +reschedule() : void
}

abstract class ProblemSolutionBase

class FJSP2Solution {
  +getWorkBalancing() : double
  +getSystemCost() : double
  +getDecisionOf(product) : ProductDecision
  +getDecisionOf(operation) : OperationDecision
  +verify() : boolean
}

interface DecisionContext {
  +getModel() : ManufactureFactory
  +getMachineSTManager() : MachineStatusManager
  +getResourceStatusManager() : ResourceStatusManager
  +getJobStatuses() : List<JobStatus>
  +getCostController() : CostControlProvider
  +getMachineSeizer() : MachineSeizer
  +getResourceSeizer() : ResourceSeizer
}

interface ProductDecision

interface MachineDecision {
  +getMachine() : Machine
  +getStartTime() : double
  +getEndTime() : double
  +getTotalWorkTime() : double
  +first() : OperationDecision
  +last() : OperationDecision
  +dump(writer) : void
}

interface OperationDecision {
  +getIndex() : int
  +getOperation() : Operation
  +getParent() : MachineDecision
  +getAssignTime() : double
  +getEndTime() : double
  +getSetupTime() : double
  +getConfiguration() : MachiningConfiguration
  +getPriority() : int
}

interface ResourceDecision {
  +getResource() : ResourceStatus
  +getChangeCost() : double
  +getChangeTime() : double
  +getFixCost() : double
  +isChanged() : boolean
  +getFrom() : MachineStatus
  +getTo() : MachineStatus
  +getOperationDecision() : OperationDecision
}

interface ResourceStorageDecision
interface MachineStatus
interface ResourceStatus
interface JobStatus
interface MachineStatusManager
interface ResourceStatusManager
interface MachineSeizer
interface ResourceSeizer
interface CostControlProvider

class CriticalPath
class ManufactureFactory
class Product
class Operation
class Machine
class MachiningConfiguration

IProblemSolution <|-- IFJSP2Solution
ProblemSolutionBase <|-- FJSP2Solution
IFJSP2Solution <|.. FJSP2Solution

FJSP2Solution "1" *-- "0..*" ProductDecision : productDecisions
FJSP2Solution "1" *-- "0..*" MachineDecision : machineDecisions
FJSP2Solution "1" *-- "0..*" ResourceStorageDecision : resourceDecisions
FJSP2Solution --> ManufactureFactory : model
FJSP2Solution --> CriticalPath : criticalPath
FJSP2Solution --> "0..*" OperationDecision : opSortedSequence

DecisionContext --> ManufactureFactory : model
DecisionContext "1" *-- "0..*" JobStatus : jobStatuses
DecisionContext --> MachineStatusManager : machineSTManager
DecisionContext --> ResourceStatusManager : resourceStatusManager
DecisionContext --> MachineSeizer : machineSeizer
DecisionContext --> ResourceSeizer : resourceSeizer
DecisionContext --> CostControlProvider : costController

ProductDecision --> Product : product
MachineDecision --> Machine : machine
MachineDecision "1" *-- "0..*" OperationDecision : sequence
OperationDecision --> Operation : operation
OperationDecision --> MachineDecision : parent
OperationDecision --> MachiningConfiguration : configuration
ResourceDecision --> ResourceStatus : resource
ResourceDecision --> MachineStatus : fromTo
ResourceDecision --> OperationDecision : operationDecision
@enduml
```

## 4. RCPSP 与不确定性扩展

```plantuml
@startuml
left to right direction
skinparam classAttributeIconSize 0

interface ManufactureFactory
class ManufactureFactoryImpl
interface MachiningConfiguration
interface IFJSP2Solution
class FJSP2Solution

interface IRCPSPModel {
  +setProjectId(projectId) : void
  +getProjectId() : int
  +getProject() : Product
  +numOfActivities() : int
  +getActivtity(operationId) : Operation
  +getModeCount() : int
  +isSingletonMode() : boolean
}

class RCPSPModel {
  -projectId : int
  -modeCount : int
  -initialized : boolean
  +setModeCount(modeCount) : void
  +init() : void
}

interface ActivityConfiguration {
  +getFailingProbability() : double
  +setFailingProbability(failingProbability) : void
}

class ActivityConfigurationImpl
class ActivityResourceManager

interface IRCPSPScheudling {
  +getResourceBalancing() : double
}

class RCPSPScheduling {
  -resourceBalancing : double
  +getResourceBalancing() : double
}

interface IUncertainRCPSPModel {
  +setFailingProbability(failingProbability) : void
  +getFailingProbability() : float
  +getNodeDomainSize() : int
  +getEdgeDomainSize() : int
  +isFailedOn(selOperation) : boolean
  +samplingSize() : int
  +getScenarioManager() : ScenarioManager
}

class UncertainRCPSPModel {
  -failingProbability : float
  -scenarioSize : int
  -scenarioManager : ScenarioManager
  +setScenarioSize(scenarioSize) : void
  +onInit() : void
}

interface IScenario {
  +getId() : int
  +isFailed(activityId, modeId) : boolean
}

class Scenario {
  -id : int
  -benchmarkId : String
  -failedMatrix : boolean
  -processingTimeMatrix : double
  +setValue(activityId, modeId, failed) : void
  +saveScenario(folderName) : void
}

class ScenarioManager {
  -scenarios : ArrayList<Scenario>
  -model : IUncertainRCPSPModel
  +trytoLoad(size) : void
  +save() : void
  +get(index) : Scenario
  +size() : int
}

class Product
class Operation

ManufactureFactory <|-- IRCPSPModel
ManufactureFactoryImpl <|-- RCPSPModel
IRCPSPModel <|.. RCPSPModel

MachiningConfiguration <|-- ActivityConfiguration
ActivityConfiguration <|.. ActivityConfigurationImpl

IFJSP2Solution <|-- IRCPSPScheudling
FJSP2Solution <|-- RCPSPScheduling
IRCPSPScheudling <|.. RCPSPScheduling

IRCPSPModel <|-- IUncertainRCPSPModel
RCPSPModel <|-- UncertainRCPSPModel
IUncertainRCPSPModel <|.. UncertainRCPSPModel

IScenario <|.. Scenario
UncertainRCPSPModel "1" *-- "1" ScenarioManager : scenarioManager
ScenarioManager "1" *-- "0..*" Scenario : scenarios
ScenarioManager --> IUncertainRCPSPModel : model

RCPSPModel --> ActivityResourceManager : resourceManger
IRCPSPModel --> Product : project
IRCPSPModel --> Operation : activity
UncertainRCPSPModel --> Operation : failed check
@enduml
```

## 5. SA 策略与 EC Runtime 关系

```plantuml
@startuml
left to right direction
skinparam classAttributeIconSize 0

interface IECOperation
interface IECStrategy
interface IECOptimizator
abstract class AbstractECStrategy
class SearchingStrategy
abstract class ECOptimizatorBase

interface ISAStrategy {
  +getNeighborSize() : int
  +getDefaultOptimizator() : ISAOptimizator
  +getTemperature() : double
  +getCoolingRate() : double
  +getVirtualPopsize() : int
}

class ECSAStrategy {
  -temperature : double
  -coolingRate : double
  -neighborSize : int
  -virtualPopsize : int
  -optimizator : ISAOptimizator
  +doPerform() : void
}

interface ISAOptimizator

class ECSAOptimizator {
  -temperature : double
  -coolingRate : double
  -maxIteration : int
  -iterationCount : int
  +generateNeighbour(curState) : IOffsprings
  +anneal(curState, newState, temperature) : boolean
  +doPerform() : void
}

interface ISAConfiguration
class SAConfiguration
interface ISAConfigurationLoader
class SAConfigurationLoader

IECOperation <|-- IECStrategy
IECOperation <|-- IECOptimizator
IECStrategy <|.. AbstractECStrategy
AbstractECStrategy <|-- SearchingStrategy
SearchingStrategy <|-- ECSAStrategy
IECStrategy <|-- ISAStrategy
ISAStrategy <|.. ECSAStrategy

IECOptimizator <|.. ECOptimizatorBase
ECOptimizatorBase <|-- ECSAOptimizator
IECOptimizator <|-- ISAOptimizator
ISAOptimizator <|.. ECSAOptimizator

ECSAStrategy "1" *-- "1" ISAOptimizator : optimizator
ECSAOptimizator --> ISAStrategy : strategy
ECSAOptimizator --> ISAConfiguration : configuration

ISAConfiguration <|.. SAConfiguration
ISAConfigurationLoader <|.. SAConfigurationLoader
@enduml
```

## 6. PolicyTree 工具模型与视图

```plantuml
@startuml
left to right direction
skinparam classAttributeIconSize 0

interface PTItem
interface PTTreeNode
interface PTTreeEdge
interface PTPolicyTree

class PTItemImpl
class PTTreeNodeImpl
class PTTreeEdgeImpl
class PTPolicyTreeImpl

interface PolicyTreeFactory
class PolicyTreeFactoryImpl

interface PolicyTreePackage
class PolicyTreePackageImpl

class PolicyTreeView
class PolicyTreeContentProvider
class PolicyTreeLabelProvider
class NodeFigure
class TreeLayoutActions

class ViewPart
class AbstractZestEntityContentProvider
class AbstractZestStyleFigureProvider
class Ellipse
class Action

PTItem <|-- PTTreeNode
PTItem <|-- PTTreeEdge
PTItem <|.. PTItemImpl
PTTreeNode <|.. PTTreeNodeImpl
PTTreeEdge <|.. PTTreeEdgeImpl
PTPolicyTree <|.. PTPolicyTreeImpl

PTItemImpl <|-- PTTreeNodeImpl
PTItemImpl <|-- PTTreeEdgeImpl

PolicyTreeFactory <|.. PolicyTreeFactoryImpl
PolicyTreePackage <|.. PolicyTreePackageImpl

ViewPart <|-- PolicyTreeView
AbstractZestEntityContentProvider <|-- PolicyTreeContentProvider
AbstractZestStyleFigureProvider <|-- PolicyTreeLabelProvider
Ellipse <|-- NodeFigure
Action <|-- TreeLayoutActions

PTPolicyTreeImpl "1" *-- "0..*" PTTreeNode : nodes
PTPolicyTreeImpl "1" *-- "0..*" PTTreeEdge : edges
PTTreeEdge --> PTTreeNode : source
PTTreeEdge --> PTTreeNode : target
PolicyTreeView --> PolicyTreeContentProvider : content provider
PolicyTreeView --> PolicyTreeLabelProvider : label provider
PolicyTreeLabelProvider --> NodeFigure : figure
PolicyTreeView --> TreeLayoutActions : layout action
@enduml
```

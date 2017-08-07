# Command Pattern

## Intent
Encapsulate a request as an object to allow clients to be parameterised with different requests.

## Reasons
To be able to issue requests to objects without knowing anything about the operation being requested, or the receiver of the request.

## Uses
1. Specify, queue, and execute requests at different times.
1. Support undo: Command's `execute` operation can store state in the Command object itself for reversing its effects via an `unexecute` or `undo` operation in the Command interface. Executed commands are stored in a history list.
1. Support logging changes so that they can be reapplied in case of a system crash. The Command interface will need `load` and `store` operations. Recovering from a crash involves reloading logged commands and re-executing them with the `execute` operation.
1. Macro recording: Record a sequence of actions by keeping a list Command objects as they are executed. The actions can then by played back by executing the same Command objects in sequence.

## Benefits
1. Decouples the object that invokes the operation from the one that performs it.
1. Commands are first-class objects - can be manipulated and extended like any other object.
1. Commands can be assembled into a composite command.
1. Easy to add new Commands - existing classes do not need to be changed.

## Participants
**Client**
* Holds Invokers, Commands and Receivers.
* Decides Receivers that are assigned to Commands, and Commands that are assigned to Invoker.
* Decides the commands to execute at the right times.

**Invoker**
* Knows how to execute a Command, but does not know anything about ConcreteCommand.
* Optionally does bookkeeping about the Command execution.

**Command**
* Interface for executing an operation.

**ConcreteCommand**
* Invokes operations on its Receiver to carry out the request.
* Values for parameters of the Receiver are stored here.

**Receiver**
* Does the work when `execute` in Command is called.

## Sources
* Design Patterns: Elements of Reusable Object-Oriented Software by Erich Gamma, John Vlissides, Ralph Johnson, Richard Helm
* https://en.wikipedia.org/wiki/Command_pattern
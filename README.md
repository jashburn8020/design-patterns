# Design Principles and Patterns

- [Design Principles and Patterns](#design-principles-and-patterns)
  - [Single Responsibility Principle (SRP)](#single-responsibility-principle-srp)
    - [SRP Examples](#srp-examples)
  - [Open-Closed Principle (OCP)](#open-closed-principle-ocp)
    - [OCP Examples](#ocp-examples)
  - [Liskov Substitution Principle (LSP)](#liskov-substitution-principle-lsp)
    - [LSP Examples](#lsp-examples)
  - [Interface Segregation Principle (ISP)](#interface-segregation-principle-isp)
    - [ISP Examples](#isp-examples)
  - [Dependency Inversion Principle (DIP)](#dependency-inversion-principle-dip)
    - [DIP Examples](#dip-examples)
  - [Builder](#builder)
    - [Builder Examples](#builder-examples)
  - [Factory](#factory)
    - [Factory Examples](#factory-examples)
  - [Prototype](#prototype)
    - [Prototype Examples](#prototype-examples)
  - [Singleton](#singleton)
    - [Singleton Examples](#singleton-examples)
  - [Adapter](#adapter)
    - [Adapter Examples](#adapter-examples)
  - [Bridge](#bridge)
    - [Bridge Examples](#bridge-examples)
  - [Sources](#sources)

## Single Responsibility Principle (SRP)

A class should have only 1 reason to change. Responsibility implies a reason for change.

### SRP Examples

Python:

- [`srp_violate.py`](python/src/srp/srp_violate.py)
- [`srp_comply.py`](python/src/srp/srp_comply.py)
- [`srp_test.py`](python/src/srp/srp_test.py)

## Open-Closed Principle (OCP)

Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.

### OCP Examples

Python:

- [`ocp_violate.py`](python/src/ocp/ocp_violate.py)
- [`ocp_comply.py`](python/src/ocp/ocp_comply.py)
- [`ocp_test.py`](python/src/ocp/ocp_test.py)

## Liskov Substitution Principle (LSP)

Subtypes must be substitutable for their base types.

### LSP Examples

Python:

- [`lsp_test.py`](python/src/lsp/lsp_test.py)

## Interface Segregation Principle (ISP)

Clients should not be forced to depend on methods that they do not use.

### ISP Examples

Python:

- [`isp_violate.py`](python/src/isp/isp_violate.py)
- [`isp_comply.py`](python/src/isp/isp_comply.py)
- [`isp_test.py`](python/src/isp/isp_test.py)

## Dependency Inversion Principle (DIP)

High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.

### DIP Examples

Python:

- [`dip_violate.py`](python/src/dip/dip_violate.py)
- [`dip_comply.py`](python/src/dip/dip_comply.py)
- [`dip_test.py`](python/src/dip/dip_test.py)

## Builder

- When piecewise object construction is complicated, provide an API for doing it succinctly
- Motivation
  - some objects are simple and can be created in a single initialiser call
  - other objects require a lot of ceremony to create
  - having an object with 10 initialiser arguments is not productive
    - instead, opt of piecewise construction
  - Builder provides an API for constructing an object step-by-step

### Builder Examples

Python:

- [`builder.py`](python/src/builder/builder.py)
- [`builder_test.py`](python/src/builder/builder_test.py)
- [`builder_facets.py`](python/src/builder/builder_facets.py)
- [`builder_facets_test.py`](python/src/builder/builder_facets_test.py)
- [`builder_inheritance.py`](python/src/builder/builder_inheritance.py)
- [`builder_inheritance_test.py`](python/src/builder/builder_inheritance_test.py)

## Factory

- Motivation
  - object creation logic becomes too convoluted
  - initialiser is not descriptive
    - cannot overload with the same sets of arguments with different names
    - can turn into 'optional parameter hell'
- Wholesale object creation (not piecewise like Builder) can be outsourced to:
  - a separate method (Factory Method)
    - a static method that creates objects
  - a separate class (Factory)
    - any entity that can take care of object creation
  - a hierarchy of factories (Abstract Factory)
    - correspond to a hierarchy of types

### Factory Examples

Python:

- [`factory_method.py`](python/src/factory/factory_method.py)
- [`factory_method_test.py`](python/src/factory/factory_method_test.py)
- [`factory.py`](python/src/factory/factory.py)
- [`factory_test.py`](python/src/factory/factory_test.py)
- [`abstract_factory.py`](python/src/factory/abstract_factory.py)
- [`abstract_factory_test.py`](python/src/factory/abstract_factory_test.py)

## Prototype

- Motivation
  - when it's easier to copy an existing object to fully initialise a new one
- Prototype - a partially or fully initialised object that you copy (clone) and make use of
- We make a copy (clone) of the prototype and customise it
  - requires ['deep copy'](https://docs.python.org/3/library/copy.html#copy.deepcopy) support
- We make cloning convenient (e.g., via a Factory)

### Prototype Examples

Python:

- [`prototype_test.py`](python/src/prototype/prototype_test.py)
- [`prototype_factory_test.py`](python/src/prototype/prototype_factory_test.py)

## Singleton

- A component that is instantiated only once
- Motivation
  - for some components it only makes sense to have one in the system
    - database repository
    - object factory
  - the initialiser call is expensive
  - object represents a resource and there is only one instance of the resource
- Provide everyone with the same instance
  - prevent anyone creating additional copies
- Lazy instantiation
  - initialise only when someone actually asks for it

### Singleton Examples

Python:

- [`singleton_decorator_test.py`](python/src/singleton/singleton_decorator_test.py)
- [`singleton_metaclass_test.py`](python/src/singleton/singleton_metaclass_test.py)
- [`monostate_test.py`](python/src/singleton/monostate_test.py)

## Adapter

- Adapt the interface you are given to the interface that you actually need

### Adapter Examples

Python:

- [`adapter_test.py`](python/src/adapter/adapter_test.py)

## Bridge

- Connecting components together through abstraction
- Prevents a 'Cartesian product' complexity explosion
  - example:
    - base class: ThreadScheduler
    - can be preemptive or cooperative
    - can run on Windows or Unix
    - 2x2 scenario: WindowsPTS, UnixPTS, Windows CTS, UnixCTS
- A mechanism that decouples an interface/abstraction from the implementation
  - both can be hierarchies but they don't have to engage in one big inheritance relationship
  - you can have some inheritance and also some aggregation or just keeping references to other components

### Bridge Examples

Python:

- [`bridge_test.py`](python/src/bridge/bridge_test.py)

## Sources

- Nesteruk, Dmitri. "Design Patterns in Python for Engineers, Designers, and Architects." _Udemy_, Udemy, Inc., Aug. 2020, [www.udemy.com/course/design-patterns-python/](https://www.udemy.com/course/design-patterns-python/).

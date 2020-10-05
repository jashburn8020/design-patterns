# Design Principles and Patterns

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

## Sources

- Nesteruk, Dmitri. "Design Patterns in Python for Engineers, Designers, and Architects." _Udemy_, Udemy, Inc., Aug. 2020, [www.udemy.com/course/design-patterns-python/](https://www.udemy.com/course/design-patterns-python/).

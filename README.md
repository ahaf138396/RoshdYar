# Roshdyar

Roshdyar is an integrated platform for managing processes, requests, events, teams, and operational data within university innovation and growth centers.

The system is designed around process automation, workflow management, structured data collection, process transparency, and extensibility. Its initial focus is on addressing the operational needs of the university innovation center and growth center while providing a foundation for future analytics, reporting, and decision-support capabilities.

---

## Overview

Innovation and growth centers typically manage a wide range of processes involving teams, companies, events, requests, documents, evaluations, and internal administrative activities.

When these processes are handled through disconnected tools such as messaging platforms, paper-based documents, informal communication, and manually maintained records, several problems arise:

- Information becomes fragmented across different platforms.
- Request status becomes difficult to track.
- Processes become dependent on individuals.
- Historical records are difficult to maintain and retrieve.
- Administrative activities become difficult to monitor.
- Structured data is not available for analysis and decision-making.

Roshdyar aims to provide a centralized system where these processes can be registered, executed, tracked, and documented in a structured manner.

The system is not intended to be limited to a traditional administrative automation tool. Its long-term direction is a process and data platform for managing the operational activities of innovation and growth centers.

---

## Objectives

The main objectives of Roshdyar are:

- Digitizing manual and paper-based processes.
- Centralizing operational information.
- Providing transparent and traceable workflows.
- Reducing dependency on informal communication.
- Reducing human errors in repetitive processes.
- Maintaining structured historical records.
- Providing centralized document and information management.
- Supporting team and company management.
- Enabling operational reporting and management monitoring.
- Establishing a foundation for future data analysis and decision support.
- Maintaining functional separation between the innovation center and growth center.
- Providing an extensible architecture for future integrations and services.

---

## Core Concepts

The core of Roshdyar is built around five fundamental concepts:

Request
   |
Workflow
   |
Actor
   |
State
   |
Log

### Request

A request represents an operational action initiated within the system.

Examples may include:

* Administrative requests
* Letters
* Permissions
* Service requests
* Equipment requests
* Other organizational processes

### Workflow

A workflow defines how a request moves through the organization.

A workflow may contain:

* Steps
* Assignments
* Reviews
* Approvals
* Rejections
* State transitions

### Actor

An actor is the user, role, or organizational unit responsible for performing an action within a workflow.

### State

Every process has a defined state that represents its current position.

Example states include:

* Registered
* Under Review
* Approved
* Rejected
* Completed

### Log

System activities are recorded as historical events.

Logs provide the foundation for:

* Process tracking
* Auditing
* Historical records
* Performance analysis
* Bottleneck identification
* Management reporting

---

## Main Modules

The complete system is designed around several functional modules.

### Event and Competition Management

Provides functionality for organizing and managing events and competitions.

Planned capabilities include:

* Event creation
* Event planning
* Participant registration
* Team registration
* Participant management
* Evaluation and judging
* Result management
* Result publication

---

### Administrative Workflow

The workflow system is one of the core components of Roshdyar.

It is responsible for:

* Request registration
* Workflow definition
* Workflow execution
* Request assignment
* Review and approval
* Rejection
* Request status tracking
* Internal correspondence

The workflow system is intended to replace manual and informal process execution with structured and traceable workflows.

---

### Innovation Center Management

This module manages processes and activities related to the university innovation center.

It is designed to support:

* Innovation team requests
* Innovation center workflows
* Center-specific users and roles
* Activity history
* Request history

---

### Growth Center Management

The growth center is managed as an operationally independent part of the platform.

It can have:

* Independent users
* Independent workflows
* Independent processes
* Center-specific policies
* Separate operational data

The innovation center and growth center share the underlying platform while maintaining functional separation.

---

### User and Access Management

This module manages users, roles, and access permissions.

Planned capabilities include:

* User management
* Role management
* Access control
* Module-level permissions
* Center-level access separation

Possible roles include:

* Administrator
* Manager
* Expert
* Judge
* Team
* Other organizational roles

---

### Team and Company Management

The system is designed to maintain structured profiles for teams and companies.

A team or company profile may contain:

* Basic information
* Members
* Activities
* Requests
* Events
* Documents
* Evaluations
* Historical interactions

The long-term goal is to provide a comprehensive operational profile for each team or company.

---

### Document and Archive Management

The document management layer provides centralized storage and organization of organizational documents.

Planned capabilities include:

* Document storage
* Categorization
* Tagging
* Document search
* Document retrieval
* Linking documents to requests
* Linking documents to events
* Linking documents to teams and companies
* Version and history management
* Access control

---

### Reporting and Management Monitoring

Roshdyar is designed to provide management with a centralized view of operational activities.

Planned capabilities include:

* Request statistics
* Process status reports
* Operational reports
* Periodic reports
* Management dashboards
* Process monitoring

---

### Performance Evaluation

The platform is designed to support future performance evaluation capabilities.

These may include:

* KPI definition
* Team evaluation
* Process evaluation
* Performance comparison
* Historical performance analysis

---

### Data Analytics and Decision Support

Structured operational data provides the foundation for future analytical capabilities.

The long-term analytics layer may provide:

* Trend analysis
* Pattern identification
* Process performance analysis
* Bottleneck detection
* Team performance analysis
* Management decision support

---

### Notification and Communication

Future versions may provide system-level notification capabilities.

Possible channels include:

* In-system notifications
* SMS
* Email
* Event notifications
* Request status notifications
* Reminders

---

### Resource and Asset Management

Resource management is considered a future expansion area.

Potential capabilities include:

* Equipment management
* Space management
* Room reservation
* Resource allocation

---

### API and Integration

Roshdyar is designed with future integration in mind.

Potential integrations include:

* University systems
* Organizational systems
* External services
* Other internal platforms

The API layer is intended to make the platform extensible without tightly coupling it to a single application.

---

## MVP Scope

The initial MVP focuses on the operational requirements of the innovation and growth centers.

### Event Management

* Event definition
* Registration
* Participant management

### Core Workflow

* Request registration
* Basic workflow execution
* Request status tracking

### Innovation Center Automation

* Innovation center processes
* Center-specific users
* Request management

### Growth Center Automation

* Independent growth center processes
* Independent users
* Separate operational workflows

### Basic Information

* Teams
* Requests
* Initial documents
* Users and roles

The MVP intentionally focuses on the operational core rather than implementing the complete long-term platform at once.

---

## Architecture

The conceptual architecture of Roshdyar is organized into several layers:

+---------------------------+
|     Presentation Layer    |
|                           |
| Admin Panel               |
| Team Panel                |
| Judge Panel               |
+-------------+-------------+
              |
+-------------v-------------+
|     Application Layer     |
|                           |
| Workflow                  |
| Events                    |
| Users                     |
| Notifications             |
| Business Logic            |
+-------------+-------------+
              |
+-------------v-------------+
|        Data Layer         |
|                           |
| Operational Data          |
| Historical Data           |
| Documents                 |
+-------------+-------------+
              |
+-------------v-------------+
|     Integration Layer     |
|                           |
| APIs                      |
| External Systems          |
+---------------------------+


The architecture is intended to remain modular and extensible.

The initial implementation should avoid unnecessary distributed-system complexity and prioritize a clean, maintainable application architecture.

---

## Design Principles

### Process First

The system should model real organizational processes rather than merely providing a collection of CRUD interfaces.

### Simple but Flexible Workflows

Workflows should remain understandable for users while providing enough flexibility to represent real processes.

### Structured Data

Information should be captured in structured forms whenever possible.

Good data quality is essential for future reporting and analytics.

### Traceability

Important operations should have a clear historical record.

Users and managers should be able to understand what happened, when it happened, and which actor performed the action.

### Separation of Concerns

Functional domains should remain logically separated even when they share the same underlying platform.

### Extensibility

The system should allow future modules, integrations, and services to be added without requiring fundamental architectural changes.

### Avoid Premature Complexity

The architecture should evolve according to actual requirements.

Complexity should be introduced when it solves a real problem rather than as an architectural goal by itself.

---

## Data Model Direction

The long-term data model revolves around the relationships between operational entities.

A simplified conceptual model can be represented as:

                    +---------+
                    |  User   |
                    +----+----+
                         |
                         |
                    +----v----+
                    | Request |
                    +----+----+
                         |
                    +----v-----+
                    | Workflow |
                    +----+-----+
                         |
              +----------+----------+
              |                     |
        +-----v-----+         +-----v-----+
        |   State   |         |    Log    |
        +-----------+         +-----------+

                    +-------------+
                    |    Team     |
                    +------+------+ 
                           |
              +------------+------------+
              |            |            |
         +----v----+  +----v----+  +----v-----+
         | Events  |  |Requests |  |Documents |
         +---------+  +---------+  +----------+


The exact implementation of the data model is determined by the current application and may evolve as the system develops.

---

## Data as a Strategic Layer

One of the long-term goals of Roshdyar is to turn operational activity into structured organizational data.

For example:

Teams
Requests
Workflows
Events
Participants
Evaluations
Documents
Users
Activities

When these entities are consistently recorded and related, the platform can gradually build a historical representation of the innovation ecosystem.

This creates the foundation for future:

* Analytics
* Reporting
* KPI calculation
* Performance evaluation
* Process optimization
* Decision support

---

## Roadmap

### Phase 1 — MVP

* Event management
* Competition management
* Core workflow
* Innovation center automation
* Growth center automation
* Request tracking
* User and role management
* Basic information management

### Phase 2 — Stabilization

* UX improvements
* Advanced notifications
* Operational reporting
* Management dashboards
* Resource management
* Improved document management

### Phase 3 — Intelligence

* Advanced analytics
* KPI
* Team scoring
* Performance analysis
* Recommendation systems
* Decision-support capabilities

### Phase 4 — Ecosystem

* External integrations
* Advanced API capabilities
* University system integrations
* Advanced dashboards
* Broader organizational use

The roadmap describes the intended direction of the platform and does not imply that all listed capabilities are currently implemented.

---

## Project Status

Roshdyar started as a proposal for a comprehensive innovation management system and progressed into an actual software project.

The MVP reached its planned completion stage on 2 Mordad 1405 (24 July 2026) and subsequently entered the evaluation phase.

The current repository should be considered the implementation of the project rather than a direct representation of the complete long-term scope described above.

---

## Relationship with Jooya

Roshdyar originated within the broader Jooya ecosystem.

The two projects have different primary purposes:

Jooya
  |
  +-- Search and Data Infrastructure
  |
  +-- Data Processing
  |
  +-- Data Insight

Roshdyar
  |
  +-- Innovation Center Operations
  |
  +-- Workflow Management
  |
  +-- Structured Operational Data

Roshdyar can potentially serve as a real-world source of structured operational data for future data analysis and insight capabilities.

Any direct integration between the two systems is considered a future integration unless explicitly implemented in the current version.

---

## Development Philosophy

Roshdyar is intended to evolve incrementally.

The development process prioritizes:

1. Solving real operational problems.
2. Keeping the core workflow understandable.
3. Maintaining high-quality structured data.
4. Avoiding unnecessary architectural complexity.
5. Keeping modules clearly separated.
6. Preserving the ability to extend the system.
7. Building advanced capabilities on top of reliable operational data.

The project is therefore not treated merely as a collection of software features. Its long-term objective is to establish a reliable digital foundation for the operational processes and data of an innovation ecosystem.

---

## Future Vision

The long-term vision of Roshdyar is to evolve from an operational automation system into a comprehensive process and data platform.

The evolution can be summarized as:

Manual Processes
       |
       v
Digital Processes
       |
       v
Workflow Automation
       |
       v
Structured Operational Data
       |
       v
Reporting and Monitoring
       |
       v
Data Analytics
       |
       v
Decision Support


This progression allows the system to create value at each stage without requiring the complete long-term architecture to be implemented from the beginning.

---

## Repository Structure

The repository structure is implementation-dependent and should reflect the actual application architecture.

The recommended organization is based on clear separation between:

* Application
* Domain modules
* Configuration
* Infrastructure
* API
* Data models
* Tests

The repository should prioritize discoverability and maintainability as the codebase grows.

---

## Installation

Installation and deployment instructions should be maintained according to the actual implementation of the current release.

This section should contain:

* Runtime requirements
* Dependency installation
* Environment configuration
* Database setup
* Development server
* Production deployment

---

## Configuration

Configuration should be provided through environment-specific settings rather than hard-coded application values.

Typical configuration areas include:

* Application settings
* Database connection
* Authentication
* External services
* Notification providers
* Storage
* Deployment settings

Sensitive credentials must never be committed to the repository.

---

## Development

A local development environment should provide the ability to:

1. Install project dependencies.
2. Configure the required environment variables.
3. Initialize the database and required services.
4. Run the application.
5. Run automated tests.

Project-specific development instructions should be kept synchronized with the actual implementation.

---

## Testing

Testing should cover the critical business logic of the system, especially:

* Workflow transitions
* Request processing
* Access control
* User roles
* Data validation
* Event registration
* Business rules

As the system grows, integration and end-to-end testing should be added for critical organizational processes.

---

## Security

Because Roshdyar handles organizational and potentially sensitive operational information, security is a core requirement.

Important areas include:

* Authentication
* Authorization
* Role-based access control
* Center-level data separation
* Input validation
* Secure file handling
* Audit logging
* Secret management
* Secure API access

Security requirements should evolve together with the system's scope and deployment environment.

---

## Documentation

Documentation should be maintained alongside the implementation.

Recommended documentation areas include:

* Architecture
* Domain concepts
* Workflow definitions
* API documentation
* Database model
* Deployment
* Development guidelines
* Operational processes

The README provides the high-level project overview; detailed technical documentation should be maintained separately where appropriate.

---

## License

License information should reflect the actual license selected for the Roshdyar repository and its components.

---

## Project Context

Roshdyar is designed as a practical implementation of an operational need within a university innovation ecosystem.

Its central idea is simple:

> Replace fragmented processes with structured workflows, turn operational activity into reliable data, and build the foundation for better management and decision-making.

 
 

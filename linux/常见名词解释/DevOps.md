# DevOps

DevOps 中涉及的技术栈与工具链如下：
DevOps (a clipped compound of development and operations) is a culture, movement or practice that emphasizes the collaboration and communication of both software developers and other information-technology (IT) professionals while automating the process of software delivery and infrastructure changes. It aims at establishing a culture and environment where building, testing, and releasing software can happen rapidly, frequently, and more reliably.
DevOps 流程门户： 这是统一操作的web网站，主要是进度看板，Sprint周期等。本着拿来主义，在一定条件下，可以采用类似Trello，worktile等工具代替。
身份及访问管理： 用户权限管理的重要组成，可以采用RABC的方式实现，也可以与LDAP服务对接
产品管理： 产品的需求，定义，依赖，推广等产品线的全面管理，confluence 可能是个不错的选择，禅道也可以满足一部分的功能
配置管理： 提高产品的配置维护能力，zookeeper 大概是不二之选。
持续集成： 提供持续集成任务调度和执行的能力，Jenkins的用武之地，提供产品和组件自动编译、打包和部署的能力，支持编译和部署的流程编制，进度跟踪和日志查看
环境管理： 提供资源配给和负载均衡的能力，需要配合云服务的资源管理能力。初级的负载均衡可以选择nginx或者Haproxy，生产环境的入口最好采用云服务的SLB负载均衡，以便简单地解决HA的问题。资源的调度采用云的弹性能力，辅助脚本实现。同时，微服务的容器化（docker）管理需要特别关注。
质量反馈： 提供产品的质量管理和监控能力，包括测试用例，缺陷跟踪和质量监控。Jira 是个不错的选择，其他的开源工具例如禅道，bugzila，mantis等等，因团队而异。
版本控制： 代码库的创建和维护，分支管理等。Git 几乎是行业的标准，可以自建Git仓库的服务器，也可以使用github 或者bitbucket这样的第三方服务。
自动化测试： 包括客户端与服务器端的自动化测试框架，例如Appium，Selenium 以及各种Mock技术和xUnit
文档管理：各种开发、运维、部署文档的统一管理，同样最好放到git上，同时指出文档的自动化生成
运营管理：这就是传说中的OAM 中心，这是广义的运营，其中还包括运维的部分。OAM 不但提供了业务系统的运营操作，还提供了面向运维的统一Monitor，alarm，fault handling等能力，以及产品的资源使用和运行状况等，涉及的技术很多，尽量采用云监控＋脚本的方式，规模较小时可以尝zZabbix 实现部分功能。
沟通管理： 敏捷的一个原则就是沟通优于文档，IM是团队必备，微信和QQ可以满足大部分的需求，但是Slack 因为其强大的web hook 功能显得更加出色。DevOps (a clipped compound of development and operations) is a culture, movement or practice that emphasizes the collaboration and communication of both software developers and other information-technology (IT) professionals while automating the process of software delivery and infrastructure changes. It aims at establishing a culture and environment where building, testing, and releasing software can happen rapidly, frequently, and more reliably.
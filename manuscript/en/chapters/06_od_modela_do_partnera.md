# 6. From language model to communication partner: architecture and application of AI agents
## 6.1 Introduction: evolution from model to agent
The development of artificial intelligence, in its essence, represents an uninterrupted path from the creation of systems that passively process information to those that act purposefully within their environment. We can follow that path through a key conceptual change: the evolution from a model to an agent. Although both terms refer to computational artifacts created to solve complex problems, their nature, purpose, and way of being in the world are fundamentally different.
By the term model in the context of machine learning and traditional artificial intelligence, we understand a mathematical or computational abstraction of a process, system or set of data. Its primary purpose is descriptive or predictive. The model takes in input data and, based on the patterns it learned during the training phase, produces an output – be it classification, regression or some other type of prediction. For example, an image recognition model can accurately determine whether there is a cat in a photo, and a prognostic model can predict the weather with a certain probability. His function is fulfilled the moment he delivers the information. It is, in essence, a passive instrument of analysis, the result of which is interpreted and based on which a person or some other, separate system acts.
However, such an approach, despite its analytical power, encounters fundamental limitations when faced with the need for autonomy and interaction in dynamic environments. The world is not a static set of data waiting to be analyzed, but a space within which it is necessary to make decisions and act. The concept of agent therefore appears as a necessary and logical step in this evolution. The agent is an observer, but also an active participant. According to the generally accepted definition, an agent is anything that can perceive its environment using sensors and act on that environment using actuators (Russell & Norvig, 2021). Its existence is determined by a continuous cycle of perception, reflection and action.
The action of the agent is guided by rationality, that is, by striving to achieve set goals. A rational agent is one who takes actions to maximize the expected measure of success, given the sequence of perceptions and knowledge at his disposal (Sutton & Barto, 2018). While for a model the key metric is *prediction accuracy*, for an agent it is *effectiveness of action*. An autonomous vehicle, for example, is an agent that uses information about the prediction of the paths of other vehicles in order to make decisions - speed up, slow down, turn - with the aim of safely and efficiently arriving at the destination.
The transition from model to agent marks a profound paradigm shift. The focus shifts from the creation of representations of the world to the development of entities that can exist and act independently in that world. Autonomy, which in the model-based approach was completely outside the system, becomes its central feature in the agent. It is possible to show this evolutionary path clearly.

![](../../docs/diagrams_en/ch06_model_vs_agent.svg)

*Figure 6.1: Contrast of the model as a passive predictor and the agent as an active participant in the feedback loop with the environment.*

In the modern age, we are witnessing how this evolution is taking place at an accelerated rate. Large language models (LLM), which in their beginning were primarily complex statistical models of language, today are increasingly incorporated into architectures that enable them to act as agents. By connecting to external tools, data sources and action capabilities, they cease to be purely text generators and become the core of reasoning within more complex agents capable of planning and executing tasks. This confirms that the development path of artificial intelligence is directed from the creation of sophisticated analytical tools towards the formation of autonomous, rational and purposeful stakeholders in the digital and physical world.

## 6.2 Programmable language: the role of the application programming interface (API) as a bridge
Application programming interface, better known by the acronym API (*Application Programming Interface*), represents a key set of rules, protocols and tools that acts as an intermediary bridge between different software applications, components or systems, enabling them to communicate with each other and exchange data in a structured and predictable way. Its basic purpose is to enable one software component to use the functionality of another, without the need to know the complexity of its internal implementation. This API establishes a clear interaction contract, defining the types of requests that can be made, the way in which these requests are formed, which data formats it uses, and what kind of response can be expected.

> **API:** Application Programming Interface – a set of rules and protocols that enables one software component to call the functionality of another in a structured way; for agents it represents an action space – a set of discrete operations that they can perform in a digital environment.

The operation of the API can be clearly demonstrated by comparing it with ordering in a restaurant. The guest in the restaurant (the client) does not communicate directly with the kitchen (the server system), but submits his order to the waiter (the API) using a menu (the API documentation) that clearly lists the available dishes and their prices. The waiter then transmits the order to the kitchen in a format it understands. After the dish is prepared, the kitchen hands it over to the waiter, who serves it to the guest. In this analogy, the guest does not need to know how the kitchen works, what the recipes are, or how the staff is organized; he relies on a clearly defined interface – the waiter and the menu – to get the desired service.


![](../../docs/diagrams_en/ch06_api_request_flow.svg)

*Figure 6.2: A communication flow in which a client sends a request to an API, the API forwards it to the server, and returns a response to the client.*

In this intermediary role, the API simultaneously performs the function of a protective layer of abstraction. It hides the complexity of the backend system and exposes only those functionalities that are necessary for interaction. Such an approach brings far-reaching advantages in software development. It allows for modularity, where different parts of the system can be developed, updated or even replaced independently of each other, as long as they adhere to the contract defined by the API. This encourages reusability of code and components and speeds up the overall development process. For example, a development team creating a mobile weather application does not need to build its own meteorological infrastructure; instead, he can make an API call to an external service that provides that data.
It is this standardized nature of the interaction that turns the API into a kind of *programmable language*. Each API call, with its specific parameters and commands, resembles an instruction within a higher-level programming language. Instead of writing complex code to, for example, process a credit card payment, the developer uses the payment service provider's API and calls a simple function like ``charge(amount, card_number)''. A sequence of such calls enables the orchestration of complex processes by combining previously built, independent functionalities.
For an agent, the API establishes an overall action space – a set of discrete operations it can perform to achieve given goals. For example, a travel planning agent learns to use publicly available APIs to search for flights, check availability, and make reservations. In this way, APIs function as abstract building blocks that enable agents to act purposefully and autonomously, turning the digital ecosystem into a programmable environment governed by defined protocols (O'Keefe, 2024).
The current practice of deploying agents based on large language models (LLM) encompasses the use of APIs in several key domains. APIs of services such as Google Search, Wikipedia and ArXiv are used to retrieve knowledge and information from external sources, which allow agents to access recent and verified data (Patil et al., 2023). In the domain of office productivity and collaboration, tools such as Microsoft Graph API and Google Workspace API enable the automation of administrative tasks. For specific software development tasks, the GitHub API provides functionality for managing repositories and project tasks. Of particular importance are API aggregation platforms, such as Zapier, which offer a unified interface for interacting with thousands of different applications. Such platforms drastically expand the capabilities of agents, enabling them to perform complex, multi-phase work processes without having to implement each individual integration (LlamaIndex, n.d.; Zapier, n.d.).
In contrast to the static, predefined integration of tools, the latest scientific and technological developments are directed towards a paradigm in which agents autonomously learn to use new APIs. Key elements of this approach are API learning techniques, as demonstrated in work on tool-augmented language models (TALM), where the model learns to use an API based on a small number of call-and-response examples (Parisi et al., 2022). Consequently, this reduces the need to manually program interactions. Another fundamental element is the standardization of tool descriptions through machine-readable manifest files (e.g. openapi.yaml), which contain a formal description of API functionality. This enables agents to perform dynamic discovery and independently integrate the tool into their own workflow. This approach repositions AI agents as primary API users, encouraging the development of interfaces that are inherently agent-friendly, thus transforming the entire network into a universal and dynamically usable set of tools (Patil et al., 2023).

### 6.2.1 API call structure
Any communication between software systems mediated by an application programming interface (API) takes place through precisely formed requests, known as API calls. These calls are a structured message composed of several key elements, each of which has a clearly defined purpose. Understanding this structure is a fundamental prerequisite for successfully interacting with any API, including those used by agent-based systems.
The central element of every call is the destination address (URL), also known as *endpoint*. It represents a unique identifier of a resource that one wants to access or perform a specific action on. A URL usually consists of the server's base address (eg `https://api.primjer.com/v1/`) and a specific path that precisely identifies the resource (eg `/users/123`).
The nature of the action itself that the caller, in our case the agent, wants to perform on the resource is expressed by the HTTP method. These methods, sometimes called HTTP verbs, define the semantics of the operation. The most frequently used methods are aligned with basic data operations (CRUD – *Create, Read, Update, Delete*):
**GET:** Used to retrieve an existing resource. This method is idempotent, meaning that repeating the same call multiple times will not change the state of the resource.
**POST:** Used to create a new resource. As a rule, each POST call results in the creation of a new, unique entity on the server.
**PATH:** It is intended to completely update an existing resource. The caller sends an entire new representation of the resource that replaces the old one.
**DELETE:** Used to delete a specific resource.
In addition to the address and method, the API call also contains headers. They transmit metadata that are necessary for the correct processing of the request, but do not constitute its central content. The headers usually contain information about authorization, such as an API key or token (`Authorization`), as well as information about the format of the content being sent (`Content-Type`) or the format expected in the response (`Accept`). Correctly set headers ensure that the server can verify the identity of the caller and correctly interpret the data it receives.
Finally, many calls, especially those using the POST and PUT methods, also contain the body of the request (*body* or *payload*). The body of the request contains specific data that is sent to the server, most often formatted in JSON (*JavaScript Object Notation*) format. For example, when creating a new user, the request body would contain information such as first name, last name and email address. In addition to the body, data can also be transmitted via parameters that are part of the URL itself. *Query* parameters (eg `?sort=asc&limit=10`) are used to filter, sort or paginate results, while *path* parameters are used to identify a specific resource within the path (e.g. user `id` in path `/users/{id}`).
All these parts together form a complete and unambiguous request that the API server can process, thus enabling the agent to perform complex tasks in interaction with external digital systems.

![](../../docs/diagrams_en/ch06_api_call_structure.svg)

*Figure 6.3: Structure of an API call from an agent to a server: HTTP method, URL, headers and request body.*

## 6.3 Anatomy of a modern communication partner
A modern communication partner, in its essence, represents a complex agent whose functionality is not exhausted in a simple exchange of information. Its structure and capabilities can be broken down into several key, interconnected components that together form a complete and effective communication entity. Understanding these components is necessary for understanding its role in the modern digital environment.

#### Deep personalization and contextual memory
One of the fundamental features of this agent is its ability to deeply personalize.

> **Personalization:** Adjusting the content, tone and behavior of the system to individual needs, interaction history and user preferences; key to engagement and perceived usefulness of communication agents.

It is not only manifested in the recognition of the user, but in the dynamic adaptation of communication to his specific needs, previous interactions and expressed preferences. Each conversation is shaped as a unique dialogue, which achieves a high level of user engagement and builds a sense of individual approach.
The ability to personalize is directly linked to the requirement for persistent contextual understanding. A modern agent must possess a kind of "memory" that goes beyond the mere retention of the last exchanged message. Its task is to integrate the entire history of interactions with the user into a single and coherent picture. This gives the communication a diachronic dimension, enabling the agent to interpret new queries in the light of previous knowledge and thus avoid repetitions and misunderstandings.

#### Affective alignment and proactive action
Communication also contains a pronounced affective component. Therefore, the anatomy of a modern agent is completed with the ability to recognize and adequately respond to the emotional state of the user.

> **Emotional intelligence:** The ability to recognize, interpret and respond appropriately to the emotional states of others; in agents, it involves analyzing tone, language choices and context to achieve empathetic and coordinated communication.

By analyzing language choices, tone or even typing speed, the agent can discern feelings such as frustration, satisfaction or confusion. In accordance with the recognized state, he adjusts his own tone and style of expression, striving to achieve the emotional harmony that is essential for building trust.
Furthermore, the passive, reactive role of waiting for the user's inquiry is replaced by a modern communication partner with a proactive approach. Based on the context and analysis of user behavior, the agent is able to anticipate future needs, offer relevant information, ask suggestive questions or suggest next steps. Such anticipatory action transforms the agent from a mere executor into a true partner in solving problems and achieving goals (Jones & Lee, 2022).

#### Multi-channel consistency and operational integration
All the listed capabilities must be applied consistently regardless of the communication channel. This principle of omnichannel consistency implies that the agent provides the same high-quality and coherent experience, whether the interaction takes place via a website, mobile application, social networks or another interface. The user must have the feeling that he is continuing the same conversation with the same interlocutor, regardless of the platform he is using at the time.
Ultimately, the backbone of the modern agent's anatomy is its deep technical integration with back-end systems.

> **CRM:** Customer Relationship Management* – a software platform that centralizes data on customers, interactions and business processes; allows agents to check orders, update profiles and initiate business actions.

Without the ability to connect to customer relationship management (CRM) systems, databases, inventory, or other business applications, an agent would be limited to providing general information. It is the integration that allows him to perform specific actions - from checking the order status and updating user data to starting more complex business processes. It thus becomes a real operational extension of the digital ecosystem.
 

![](../../docs/diagrams_en/diag_294.svg)

*Figure 6.4: Schematic representation of the key components of a modern communication agent.*

### 6.3.1 The brain of the operation: the core of LLM and the art of management
At the very center of every autonomous agent, as its neural and cognitive headquarters, is a large language model (LLM). It represents its fundamental core – the engine that drives reasoning, planning and decision-making processes. The function of LLM within the agent architecture goes beyond mere language processing; it acts as a central unit for processing complex problems, turning abstract goals into concrete, actionable steps. It is precisely in this ability that the transition from traditional programs, which follow strictly defined instructions, to systems that possess the germ of autonomy lies.
The fundamental task that is set before the LLM is decomposition. When an agent is faced with a complex task, such as organizing travel or analyzing market data, the LLM assumes the role of strategist. It decomposes the ultimate goal into a series of logical, smaller sub-tasks, thus creating a causal chain of actions. For example, the request to "research the latest trends in artificial intelligence" will break down the model into steps: first, defining key terms; second, searching relevant scientific databases and repositories; third, summarizing and synthesizing the collected information; and fourth, shaping the final report. Such hierarchical planning, which mimics human cognitive processes, allows the agent a systematic and methodical approach to problem solving (Yao et al., 2023).

> **Task Decomposition:** The process of breaking down a complex goal into a series of smaller, logically connected subtasks that can be executed sequentially or in parallel; in the context of autonomous agents, the decomposition is carried out by the LLM core acting as a strategist, turning an abstract request into a causal chain of concrete actions (Yao et al., 2023).

However, the raw power of the language model remains an unused potential without management skills, i.e. without skillfully formed prompts. The query is the basis for a structured dialogue between man and machine. The quality, precision and contextual richness of the initial query directly determines the depth and accuracy of the model's *thinking*. A poorly worded or ambiguous query can lead the agent in the wrong direction, resulting in suboptimal or completely incorrect solutions. On the other hand, a well-formed query acts as a precise instrument that directs the model's cognitive focus, encouraging it to activate relevant knowledge and apply more complex reasoning patterns.

#### The skill of formatting instructions
Before an artificially intelligent employee is entrusted with tools or access to external cognitive heritage, it is necessary to master the skill of communicating with its core. This skill, known today as **prompt engineering*, includes the art of precisely composing input orders, i.e. *prompts*, in order to extract a precisely determined answer from the vast potential space of the language model, manifest the desired behavior or adopt a given style. It stems from the very nature of large language models as refined statistical machines for predicting the next linguistic sign (token); the input instruction sets the initial conditions of that stochastic process and thereby decisively directs the path of its conclusion and expression (Liu et al., 2023a).

> **Designing instructions / prompt engineering:** The art of designing input instructions (prompts) in order to extract the desired response or behavior from the language model; it includes formulation precision, assigning a role to the model, examples (few-shot), chain-of-thought and system prompt.

Mastering the art of creating instructions rests on the application of several basic principles.
**Accuracy and semantic anchoring.** Great language models in their operation resemble extremely educated, but literal and persistent assistants. Ambiguous or overly general orders inevitably lead to undesirable or overly general responses. For example, the command "Write something about sustainability" will prompt the model to produce a general, almost random text that touches on everything from ecology to economics without any real depth. In contrast, a precisely worded order acts as a semantic anchor that directs the model towards the desired outcome: "Compose a 500-word article for a business blog about the importance of reducing plastic waste for small businesses in the hospitality industry. In the text, focus on three practical and cost-effective tips. The target audience is restaurant owners who are not experts in environmental protection. The tone should be encouraging, clear and informative." Such an instruction leaves no room for ambiguity and clearly defines the content, structure, tone and target audience.

**Assigning a role and a person** (*role-playing*). One of the most powerful techniques is to instruct the model to assume a certain role or persona (lat. *persona*). In this way, those language patterns, vocabulary and stylistic registers that were associated with that role in the learning data are activated in his vast neural network. Instruction "Act as a leading cyber security expert with 20 years of experience. Explain to the layperson the five most common threats to digital security in the home." will yield an answer that is at the same time professional, authoritative and understandable. This technique is of crucial importance for giving the employee a stable and consistent personality, which makes him a predictable and reliable communication participant.

**Providing context and examples** (*few-shot prompting*). As first demonstrated by the creators of the GPT-3 model (Brown et al., 2020), large language models possess an extraordinary ability to learn from the examples presented to them within the instruction itself. Instead of merely describing the task, providing several concrete examples (*shots*) allows the model to abstract the required pattern and apply it to a new case. This process can be graphically illustrated in the task of classifying feelings (sentiment) in the text.

> **Scheme 1:** Sample prompt with several examples (*Few-shot Prompting*)
>
> Classify the feeling in the following sentence as 'Positive', 'Negative' or 'Neutral'.
>
> **Sentence:** "The service was outstanding and the food was delicious." **Feeling:** Positive
>
> **Sentence:** "We waited too long, and the bill was wrong." **Feeling:** Negative
>
> **Sentence:** "The meeting is scheduled for Wednesday at 10 am." **Feel:** Neutral
>
> **Sentence:** "The new film completely disappointed me." **Feeling:**

After being presented with the first three examples, the model concludes with far greater confidence that the correct answer for the last sentence is "Negative".

> **Learning from examples / few-shot prompting:** A language model management technique in which several concrete examples (shots) of the desired input-output pattern are specified within the instruction itself, thereby prompting the model to abstract the required pattern and apply it to a new, unknown case; the opposite is the zero-shot approach, where no examples are given (Brown et al., 2020).

**Chain-of-Thought* (CoT).** For complex tasks that require logical or arithmetic reasoning, large language models perform significantly better if they are explicitly encouraged to break down the problem into component steps. By adding a simple phrase like "Let's think one step at a time." at the end of the instruction, the model is forced to make its inference process visible, printing it out as text. This follows a more logical path, reduces the probability of error and enables the correctness of the procedure to be checked (Wei et al., 2022). More advanced techniques, such as ReAct (Yao et al., 2023), combine such incremental thinking with the use of external tools, which forms the backbone of many contemporary worker architectures.

> **Chain of Thought / Chain-of-Thought, CoT:** A language model management technique that explicitly encourages the model to break down the problem into visible intermediate steps of reasoning before the final answer; this increases the accuracy of complex logical and arithmetical tasks and enables checking the correctness of the procedure (Wei et al., 2022).

> **Scheme 2: Comparison of Standard Instruction and Chain of Thought Instruction INPUT (Standard Instruction):** Question: There were 23 apples in the cafeteria. If they used 20 for lunch and then bought 6 more, how many apples do they have now?
>
> **OUTPUT (Probably wrong):** 29
>
>
> **INPUT (Chain of Thoughts Prompt):** Question: There were 23 apples in the cafeteria. If they used 20 for lunch and then bought 6 more, how many apples do they have now? Let's think step by step.
>
> **OUTPUT (Probably Correct):** Sure, let's think step by step.
>
> The initial number of apples is 23.
>
> They used 20 apples, so we subtract: 23 - 20 = 3.
>
> There are 3 apples left after lunch.
>
> Then they bought 6 more apples, so we do the addition: 3 + 6 = 9. The cafeteria now has 9 apples.

**System prompt** occupies a special place in model management. It is a superordinate instruction that is set at the very beginning of the interaction and that determines the general behavior, personality, powers and limitations of the model during the entire conversation. It acts as a kind of "constitution" for artificial intelligence, a set of immutable rules that the worker must adhere to.
For example, a system instruction for a specialized computer code analysis assistant could read: "You are a security analyst. Your sole purpose is to analyze the provided program code for possible security vulnerabilities according to the OWASP Top 10 list. Do not answer questions that are not related to the security of the code. Do not express personal opinions. Always format your answers as a JSON object with the fields 'vulnerability_type', 'line_number' and 'recommendation'."
A well-formed systematic instruction is essential to create a stable and reliable worker that behaves within the desired and strictly defined limits (Anthropic, 2024; OpenAI, 2024b). It is the foundation of certainty and predictability, turning a powerful but fickle linguistic core into a specialized tool with a clearly defined purpose.

> **System prompt / system prompt:** A superordinate instruction placed at the beginning of the interaction with the language model that determines its general behavior, personality, powers and limitations throughout the conversation; it acts as an agent's “constitution,” a set of immutable rules that ensure predictability, certainty, and consistency in responses (Anthropic, 2024; OpenAI, 2024b).

The art of formulating queries requires the user or developer to have a deep understanding of the problem domain and how LLM "thinks". It is necessary to anticipate possible interpretations, remove ambiguities and provide the model with enough context to make an informed decision. In this sense, the interaction with the agent is an iterative process of coordination and refinement, in which the optimal solution is gradually crystallized through a series of questions and answers.



#### From tool to cognitive partner
Through this synergy of inherent model capabilities and human management skills, LLM within the agent ceases to be a passive tool and transforms into an active cognitive partner. While traditional software tools perform precisely defined functions, the LLM-driven agent participates in the very process of defining the solution. He does not wait for a complete specification of each step, but independently proposes, analyzes and selects courses of action based on the general goal.
The effectiveness of the autonomous agent, therefore, rests on two pillars: on the one hand, on the strength and sophistication of the language model that forms its core, and on the other hand, on the skill with which a person directs that strength. Understanding this dual nature – a powerful machine and the need for its fine tuning – is the key to unlocking the full potential of autonomous systems and their successful application in solving the challenges of the modern world. Mastering this "brain of the operation" is therefore a strategic imperative.

### 6.3.2 Structure of memory in conversational systems
The ability to remember is a fundamental determinant of the effectiveness and naturalness of conversational systems. Memory in this context goes beyond data storage; it is a complex mechanism that allows the agent to follow the flow of the conversation, understand the context and provide coherent and relevant answers. Without effective memory, each interaction with the user would be reduced to a series of unrelated questions and answers, thus losing the very core of the conversation. Therefore, the structure of memory in modern conversational agents is usually divided into several levels.

#### Flow of information from sensory, through short-term, to long-term memory
In practice, the memory of conversational systems can be seen as a flow through three levels. Sensory memory serves as a short-term input filter that captures immediate stimuli and signals from the user's queries. Short-term (working) memory maintains the current context of conversation within a session, while long-term memory stores more stable facts, preferences, and patterns necessary for continuity across multiple interactions.

#### Short-term memory - context
Relevant information is transferred to short-term memory, which is often called *working memory* in the literature. It stores all the contextual data necessary to maintain coherence within a conversational session. This includes the user's last statements, the agent's responses, recognized intentions and entities, and all other elements that enable meaningful continuation of the dialogue. In terms of its function and limitations, it is comparable to the working memory (RAM) in a computer: it has a limited capacity and its contents are deleted after the end of the interaction or after a certain period of inactivity.

> **Working memory:** Short-term storage area of the conversational agent in which the contextual data of the current session is stored - user's statements, agent's responses, recognized intentions and entities; it is functionally comparable to the working memory (RAM) of a computer because it has a limited capacity and is deleted when the interaction is over.

The immediate continuity of short-term memory within one conversational session with language models is achieved by the context window mechanism. Its implementation in practice usually boils down to the systematic inclusion of the entire history of the ongoing conversation in each new call to the model.

> **Contextual window / context window:** The maximum amount of text (in tokens) that the language model can simultaneously receive and process in one call; everything inside the window constitutes the context for generating the response; overshooting requires discarding older parts of the conversation. With each new query from the user, the system not only sends that query to the model, but also attaches the entire transcript of the previous interaction. This places the model in a wider context, allowing it to refer to previously stated claims, raise coherent sub-questions and maintain consistency in tone and content.

However, this approach encounters a hard limit set by the architecture of the model itself – the size of its contextual window, i.e. the maximum amount of text (measured in tokens) that the model can simultaneously process. Once the conversation length exceeds that threshold, the oldest parts of the interaction must be discarded. That moment represents a break point, a kind of conversational amnesia, after which the model loses memory of the beginning of the conversation, which can lead to repetition or contradictory answers. The effectiveness of this mechanism therefore declines as the conversation lengthens, making it unsuitable for all but short-term, one-off interactions.

> **Scheme: Mechanism and limitation of short-term memory**
>
>
> STEP 1:
>
> User: "Good afternoon, I am interested in the history of Dubrovnik literature."
>
> Agent → LLM Prompt: "User: Good afternoon, I am interested in the history of Dubrovnik literature."
>
>
> STEP 2:
>
> The agent's answer: "Of course. Are you referring to the period of humanism and the Renaissance, or are you interested in a later period?"
>
> User: "Let's focus on the renaissance."
>
> Agent → LLM Prompt: "User: Good afternoon, I am interested in the history of Dubrovnik literature. / Agent: Of course. Do you mean the period of humanism and the Renaissance or are you interested in the later period? / User: Let's focus on the Renaissance."
>
>
> STEP N (Conversation continues...):
>
> ...the context accumulates...
>
>
> STEP N+1 (Contextual window limit reached):
>
> [The oldest part of the conversation ("Good day...") is discarded]
>
> Agent → LLM Prompt: "...[central part of conversation]... / User: And who was the most important comedian?"
>
>
> │ LIMITATION: The model no longer "knows" the initial topic of conversation. │


#### Long-term memory – vector bases
For true persistence and retention of information over longer periods of time and across multiple chat sessions, agents must rely on external data storage systems. In modern architectures, this role is most often taken over by vector databases (*vector databases*). They enable the system to create and maintain a permanent record of key information, preferences and facts related to the user, thus forming the basis for his diachronic identity within the system. The process of establishing and using long-term memory can be broken down into three key steps.

> **Vector database / vector database:** A specialized storage system that presents data as numerical vectors (embeddings) in a multidimensional space and enables quick search by semantic similarity, not by keywords; in the architecture of conversational agents, it serves as long-term memory that preserves user preferences, facts, and summaries of previous interactions across multiple sessions (Xu et al., 2023).

**1. Summarizing and extracting facts**: The system does not store the raw transcript of each conversation, as this would be unreadable and computationally demanding. Instead, the agent periodically, either after each interaction or at the end of a session, analyzes the conversation with the goal of extracting and summarizing key information. These can be explicitly stated facts (e.g. "The user's name is Ivan", "Ivan's son is studying medicine in Zagreb"), but also implicitly expressed preferences (e.g. "The user prefers concise answers", "The user is interested in ancient philosophy, especially Stoicism").

**2. Vectorization and storage**: Extracted facts and summaries are converted from textual form into numerical representations, so-called vector embeddings. Each embedding is a vector, that is, a series of numbers that represents the position of the given information in a multidimensional semantic space. This vector can be understood as a unique "semantic imprint" of the information. The data converted in this way is stored in the vector database, where each vector remains permanently recorded and linked to the user's identity.

> **Vector embedding / embedding:** Numerical representation of a text, word, sentence or document in the form of a sequence of numbers (vector) located in a multidimensional semantic space; semantically similar content has close vectors, allowing search by meaning instead of exact word match.

**3. Context retrieval and enrichment**: Before processing a new user query, the agent first searches the vector database. The search is not performed by keywords, but by semantic similarity. The agent converts the user's current query into a vector and then searches the database for stored vectors (memories) that are closest to it in the semantic space. For example, if the user asks "Can you recommend me a new book following the ones we talked about earlier?", the agent will recognize the semantic closeness of that query with the stored fact "The user is interested in ancient philosophy, especially Stoicism". The most relevant records found are retrieved from the database and inserted into the context window along with the new query. In this way, the language model obtains key information from “long-term memory” that it needs to generate a relevant and personalized response (Xu et al., 2023).

This complex mechanism allows the agent to transcend its innate ahistorical nature. Having gone beyond the status of a linguistic automaton that reacts to the current stimulus, it becomes an interlocutor that "remembers" the shared history of interactions, respects the user's specificities and thereby creates a basis for a continuous, consistent and ultimately more meaningful relationship.

### 6.3.3 Epistemic grounding: retrieval-enriched generation (RAG)
The Retrieval-Augmented Generation (RAG) approach represents an important paradigm in the field of artificial intelligence, designed for the epistemic grounding of responses generated by large language models (LLM). It is a hybrid system that combines two basic components: a mechanism for retrieving data (*retriever*) and a generative language model (*generator*). The goal of such systems is to overcome the limitations of independent language models by combining their ability to shape language with the reliability and up-to-dateness of external knowledge bases.

> **RAG:** Retrieval-Augmented Generation – a hybrid system that first retrieves relevant parts from an external knowledge base (retriever) to answer a user's query, then passes that data and the query to a language model (generator) that synthesizes the final answer; this improves the timeliness and validity of the answers.

The need for this approach stems from two fundamental shortcomings of independent large language models. The first disadvantage is the tendency to "hallucinate", that is, to generate factually incorrect or completely fabricated information, which happens when the model does not have the required information in its internal parameters. Another key disadvantage is the static nature of their knowledge base, which is limited to the data on which they have been trained and therefore does not include events or knowledge generated after their training is complete.
The RAG system operation process itself can be broken down into several key steps. The cycle starts with a user query. This query is then forwarded to the retrieval component (*retriever*), whose task is to search the external knowledge base - for example, a collection of documents, a database or Internet sources - in order to find the most relevant parts of the text or data related to the set query. This found, relevant data together with the original user query forms an enriched context that is passed to the generative language model. In the final stage, the language model (generator) synthesizes the final answer, basing it on the obtained relevant data, and not exclusively on its internal, parametric knowledge.
 

![](../../docs/diagrams_en/ch06_rag_sustav.svg)

*Figure 6.5: Schematic representation of the operation of the RAG system.*

The application of RAG architecture brings multiple advantages. The most important thing is the significant reduction in the occurrence of hallucinations, because the model directly relies on concrete, retrieved data when generating answers. Furthermore, RAG allows models to access updated or domain-specific, adapted information without the need for costly and time-consuming retraining of the entire model. This opens up the possibility of transparency and verifiability; along with the generated answer, the user can be offered the sources from which the information was taken, which allows him to check their accuracy himself. This approach is also more economical because updating the external knowledge base is much simpler and cheaper than retraining the entire language model (Lewis et al., 2020).
In the context of more complex systems, such as autonomous agents, RAG assumes the role of a key tool for informed action. When an agent is faced with a task that requires reliable and up-to-date information, it does not act hastily, but relies on the RAG mechanism to gather relevant knowledge before making a decision or formulating a response. This ensures that the agent's actions – whether it's responding to a customer's help desk inquiry or collecting data for more complex analysis – are not based on potentially outdated or inaccurate internal knowledge, but on verifiable external sources.
It should be emphasized that although the core concept of the RAG architecture is extremely powerful, its naive or simplistic application often proves insufficient for more complex problems. Therefore, a whole spectrum of advanced techniques has been developed that optimize each stage of the described process. Today, this area represents one of the most dynamic fields of research in the development of artificial intelligence (Gao et al., 2024; Barnett et al., 2024). Advanced methods of indexing and searching, techniques of intelligent classification (reranking) of retrieved documents by importance, as well as strategies for summarizing and synthesizing information from several different sources are being researched.

### 6.3.4 Hands for action: using tools as a leap in power

> **Tool Use:** The AI agent's ability to call external tools (APIs, search engines, calculators, databases) during task execution; the model decides when and which tool to call, passes parameters, and uses the result to continue reasoning; a key component of agent architectures (e.g. ReAct).

The human hand, viewed in its anatomical and functional complexity, goes beyond the role of a grasping organ and asserts itself as primarily a tool of action. Her ability for fine motor adaptation, precise manipulation and firm grip is a fundamental prerequisite for one of the most important transitions in human development: the conscious use of tools. With this act, man becomes a being who actively shapes, adapts and transcends the world. Serving as a tool therefore represents a radical change in the relationship between man and the world, a true step forward in power that opens the way to the construction of culture and technology.
This transformation deeply affects the very structure of human perception. Philosophical phenomenology has offered insightful insights into the nature of that process. Martin Heidegger introduces a distinction between tools as something *ready-to-hand* (German *Zuhandenheit*) and objects as something simply *present* (German *Vorhandenheit*). When we skillfully use a hammer, it does not exist for our consciousness as a separate object with certain properties, but recedes into the background and becomes an imperceptible extension of our hand focused on the act of driving a nail. The tool, fused with action, becomes transparent and opens the world to us not as a collection of objects to observe, but as a field of possibilities for action.
On this track, Maurice Merleau-Ponty (1962) further develops the thought of the embodiment of the tool, arguing that the body includes it in its own body scheme. The classic example of the blind man's cane clearly shows this phenomenon: for the blind man, the cane is an extension of his sensory apparatus with which he *feels* and explores the space in front of him. The tip of the stick becomes the new boundary of his body. In this way, the tool is transformed from an external object into an integral part of a person's perceptive and active field.

Through this process of fusion of body and tool, man is transformed into a significantly more powerful *agent*. His relationship with the world is no longer determined solely by the biological limits of his body. The ax extends the strength and reach of the hand, the spear enables hunting at a distance, and the letter transcends the transience of speech and memory. Each new tool opens up new ways of being in the world and acting on it. This fundamental ability to use tools is therefore found at the very origin of human history as a history of creation, transformation and overcoming the given, confirming man as a being who is constantly rebuilding his world.
![](../../docs/diagrams_en/ch06_tool_extension.svg)

*Figure 6.6: Expanding action by adopting tools: by integrating tools, the agent expands the action space and increases effectiveness.*

For language models, it is the use of tools that breaks these constraints, allowing the language model to reach outside itself and engage with living, changing systems. The foundation of this ability rests on a circular process of thinking and acting, most clearly exemplified in frameworks such as ReAct (*Reasoning and Acting*). In this cycle, the language model forms a sequence of internal reflections (*thoughts*) and external interventions (*actions*) that gradually lead it to a solution (Yao et al., 2023). This process takes place in a loop that can be repeated if necessary:



> **Fundamental cycle of reflection and action (ReAct)**
>
> **USER ACCOUNT:** "What will the weather be like tomorrow in London?"
>
> **1. THOUGHT (Reflection):** "A user asks for the weather in London. I don't have access to real-time data. I need to use the `weather_forecast_api' tool."
>
> **2. ACTION:** Creating calls to tools: `{ "tool_name": "weather_forecast_api", "tool_input": { "city": "London", "date": "tomorrow" } }`
>
> **3. OBSERVATION (Feedback):** The external system executes the call and returns the result: `{ "temperature": "15°C", "state": "Cloudy" }`
>
> **4. THOUGHT (Synthesis):** "I have received an observation. The temperature is 15°C and the weather is cloudy. I now have all the ingredients for a complete answer."
>
> **5. FINAL ANSWER:** "Tomorrow in London it will be cloudy with a temperature of 15°C."

![](../../docs/diagrams_en/ch06_tool_feedback.svg)

*Figure 6.7: Feedback from the external system in the agent cycle (Tool Use - observe).*

This circle allows the agent to solve various tasks, from everyday queries to highly specialized domains. In the role of a personal assistant, the agent can manage the calendar, send e-mail or monitor smart devices in the home. As a travel planner, he can search for flights via airline APIs, compare prices, check hotel availability and finally make a reservation. In the field of expert analysis, it is capable of executing Python scripts for complex data processing, sending SQL queries to large databases or summarizing the content of web pages accessed in real time.
The ultimate manifestations of this ability are seen in action on the physical world, where the agent's instructions, translated into machine code, control laboratory equipment, industrial robots on the production line, or agricultural drones.

### 6.3.5 Active agent: harmony of abilities
The term active agent (*agent*) in its essence includes a complex entity whose action cannot be reduced to the mere sum of its components. It is about a subject who notices his own environment, acts on it purposefully and learns from the consequences of these actions, adjusting his future actions. The fundamental principle that enables such action is the harmony of abilities - the dynamic and pervasive harmony of several key functions that together form a unique system. Without such alignment, the active agent remains just a collection of disconnected mechanisms, incapable of meaningful and adaptive interaction with the world.
The first basic ability is perception. It represents a window into the world, a channel through which the agent collects information about the state of the environment and about its own position within it. Perception is an active process of selecting, interpreting and organizing sensory information in order to create a coherent internal representation of external reality (Gibson, 1979). The raw data obtained by the senses is only a starting point that must be interpreted in the light of previous knowledge and current goals. It is precisely this interpretative nature of perception that makes it inseparable from cognitive processes.

Perception is followed by cognition, which includes the mental processes of reasoning, planning, decision-making and memory. Within this framework, received information is processed, linked to existing knowledge and used to shape intentions and action strategies. The ability to create and evaluate different possible actions is essential for intelligent behavior (Russell & Norvig, 2020). Cognition thus transforms perceptual data into purposeful plans, forming a bridge between what is and what should be done. It is the central mechanism that allows the agent to go beyond immediate reactions to stimuli and to act thoughtfully, with an eye on the future.

Plans shaped by cognition are realized through action, i.e. through the agent's ability to influence the environment and change it. Action can take different forms, from simple motor actions to complex communicative acts. It closes the circle of interaction with the world: every action causes changes in the environment, and these changes become a new object of perception. This creates an unbroken feedback loop, where action not only achieves goals, but also creates new information that enriches and changes the internal model of the world (Powers, 1973).

![](../../docs/diagrams_en/ch06_agent_cycle.svg)

*Figure 6.8: Agent-environment interaction loop: perception leads to cognition and action, and action creates new information for the next perception.*

After all, the entire system is imbued with the ability to learn, which enables continuous adaptation and improvement. Learning is the process by which the agent changes its knowledge, skills and strategies based on experience, that is, based on the outcome of its own actions. Without learning, the agent would be condemned to repeat the same mistakes, unable to adapt to new and unforeseen circumstances. The ability to learn allows it to become more resilient, more efficient and, over time, increasingly skilled in achieving its goals (Sutton & Barto, 2018).

The true nature of an active agent, however, is not manifested in individual abilities, no matter how developed they are. Its essence lies in their harmony and interdependence. Perception is aimless without knowledge to give it meaning; cognition is powerless without action that would put its intentions into effect; action is blind without a reason to direct it; and the whole assembly is static and rigid without learning that gives it adaptability and a developmental dimension. It is precisely in this constant and coordinated interweaving of perception, cognition, action and learning that an active agent capable of meaningful existence in a complex and changing world is born.
Frameworks like *LangChain* or models with strong reasoning capabilities, like OpenAI's o3, Anthropic's Claude or Google's Gemini 2.5, offer a technical foundation and structure for managing such complex interplays, along with access to tools. To make this harmony of abilities more evident, let's consider a complex example. Let's imagine that the user, let's call her Ana, sets the following task for her personal assistant: to plan an independent trip to Paris during the first weekend in October. Her preferences are art, especially impressionism, but her budget is strictly limited to approximately 500 euros for airfare and accommodation. It is also a requirement that the accommodation be in the center of the city. Let's see how an advanced agent would align its capabilities to fulfill such an order.

**1. Degree**: Thinking and imagining (Mind)
The language core of the agent first subjects Ana's query to an in-depth analysis. Using her Chain-of-Thought-like thinking ability, she breaks down a complex goal into a series of smaller, achievable and actionable sub-tasks. That initial internal monologue is the foundation of the entire operation.

> **Scheme 1: Target decomposition**
> Main goal: to plan a weekend trip to Paris (first weekend in October, solo, art/impressionism, budget ~€500, central accommodation).
>
> **Sequence of thought (internal decomposition):** Determine the correct dates: Determine which days are the "first weekend in October".
>
> **Check logistics (flight):** Search and find the best return flights for the given dates.
>
> **Check logistics (accommodation):** Find affordable and centrally located accommodation for the same dates.
>
> **Comply with the budget:** Check whether the sum of flight and accommodation costs does not exceed the default limit of 500 euros.
>
> **Explore interests:** Explore museums and landmarks related to Impressionism.
>
> **Put together a proposal:** Create a clear and coherent itinerary.
>
> **Synthesize the answer:** Form all the collected data into a final, personalized answer for the user.
>
>

**2.** Degree: Action and use of tools (Hands)
The agent immediately realizes that he lacks external, changing data in real time to fulfill the task. Therefore, he has to reach for his tools, that is, for application programming interfaces (APIs) that enable him to access external databases.

> **Scheme 2: Sequence of tool use**
> Thought sequence: "I'm missing information on flight and hotel prices. I need to call the appropriate tools."
>
> **Action 1:** Flight search tool call Command: flight_search_api.call()
>
> **Parameters:** { destination: "Paris, France", departure_date: "2025-10-03", return_date: "2025-10-05", class: "economy" }
>
> **Output (observation 1):** The tool returns a list of available flights. The cheapest option is €150 (return ticket).
>
> **Action 2:** Call the accommodation search tool Order: hotel_booking_api.call()
>
> **Parameters:** { city: "Paris", check-in_date: "2025-10-03", check-out_date: "2025-10-05", maximum_price: 350, location: "central", accommodation_type: "hotel/apartment" }
>
> **Output (observation 2):** The tool returns a list of available accommodation units. A few meet the criteria.
>
>

**3. Degree**: Reaching for knowledge and memory (Experience)
Once the logistical framework of the trip is set and confirmed within the budget, the agent turns to the more refined part of the task: adapting to Ana's personal preferences. Here comes to the fore the combination of two forms of knowledge - that stored in the long-term memory of the users and that obtained from external sources through foundation.

> **Scheme 3: Linking memory and grounded knowledge (RAG)**
> Thought sequence: "Logistics taken care of. Now I need to focus on impressionism and personalize the plan."
>
> **Action 3:** Query long-term memory Command: memory_storage.query()
>
> **Parameters:** { user_id: "Ana", keywords: ["art", "Paris", "impressionism"] }
>
> **Outcome (Observation 3):** Memory returns a record from the previous interaction: {"record": "User Ana rated the visit to the Musée d'Orsay very positively.", "date": "2024-03-12"}.
>
> **Action 4:** Query the Establishment System (RAG) Command: web_search_tool.call()
>
> **Parameters:** { query: "impressionist art museums in Paris other than Musée d'Orsay" }
>
> **Outcome (Observation 4):** The system searches verified sources and retrieves summary information about the *Marmottan Monet* (largest collection of Monet works) and *Orangerie* (famous for Water Lilies) museums, including opening hours, ticket prices, and location.
>
>

**4. Degree**: Synthesis and Communication (Voice)
With all the data collected, processed and contextualized, the language core now takes on the role of ultimate storyteller. It no longer decomposes, but combines - flight, accommodation, budget, personal preferences and newly explored possibilities - into a unique, coherent and attractive proposition.

> **Scheme 4: Final synthesis and shaping of the answer**
>
> **Thought:** "I found a flight and accommodation within the given budget. I know from memory that the user appreciates the Musée d'Orsay, and through research I found two other related museums. I can put together a complete proposal that ties all the elements together."

**Final answer (generated for Ana):**
"Dear Ana, I have prepared a proposal for your weekend in Paris, guided by your wishes and budget.
**Flight and accommodation:** I found a return flight for €150. In addition, I suggest staying in a charming studio in the Le Marais district, available through the Airbnb platform, at a price of €320 for two nights. The accommodation is excellently rated and is located in the very heart of the city. The total cost is €470, which is within your budget.
**Artistic itinerary:** Since I know your penchant for impressionists, you can dedicate Saturday to revisiting your favorite museum, the *Musée d'Orsay*. For Sunday, I suggest a visit to the museum *Musée Marmottan Monet*, which houses the world's largest collection of works by Claude Monet, including the famous painting *Impression, Rising Sun*.
Would you like me to make a flight and accommodation reservation for you?"

The presented sequence of actions reveals a problem-solving system that demonstrates the ability to align its resources and skills to achieve a given goal in a manner that is simultaneously efficient, adaptive, and reliable.
![](../../docs/diagrams_en/diag_725.svg)

*Figure 6.9: Sequence of actions of an agent when planning a personalized trip.*

### 6.3.6 Conclusion: the birth of a communication partner
The discussion so far has followed a complex path that leads from a set of program commands and data structures to the emergence of an entity that we can rightly call a communication partner. This transition, described as *birth*, metaphorically describes an actual qualitative leap in the nature of human-agent interaction. The agent assumes the role of an active participant in the act of communication. Its birth is the result of gradual maturation through a series of interactions, learning and adaptations.
The fundamental components of this process are the agent's ability to interpret the context, recognize the user's intentions and adjust its responses. At the moment when the user begins to recognize functionality in the agent, but also a kind of stability, predictability and, ultimately, reliability, the foundations for a partnership are laid. This relationship is based on the functional equivalence of communication roles. An agent becomes a partner not because he *is* human, but because he *acts* as a credible interlocutor within the given communication framework. This opens up space for more complex forms of cooperation, where trust and mutual understanding are built through continuous dialogue. It is this transformation from a tool to an interlocutor that is the key achievement that we tried to shed light on, and its path can be summarized in the following presentation.
---

![](../../docs/diagrams_en/ch06_partner_development_phases.svg)

*Figure 6.10: Stages of development of a communication partner from the linguistic core to an autonomous, integrated interlocutor.*

This concludes the theoretical consideration of the conditions under which a communication partner is created. With the theoretical framework clearly established, we turn to its application and implementation in real systems.
# Glossary

This section lists key terms used in the book with short definitions. Entries are drawn from chapters 1–8; in the main text they appear at first mention.

---

**1. THOUGHT (Reflection)** — "A user asks for the weather in London. I don't have access to real-time data. I need to use the `weather_forecast_api' tool."

**2. ACTION** — Creating calls to tools: `{ "tool_name": "weather_forecast_api", "tool_input": { "city": "London", "date": "tomorrow" } }`

**3. OBSERVATION (Feedback)** — The external system executes the call and returns the result: `{ "temperature": "15°C", "state": "Cloudy" }`

**4. THOUGHT (Synthesis)** — "I have received an observation. The temperature is 15°C and the weather is cloudy. I now have all the ingredients for a complete answer."

**5. FINAL ANSWER** — "Tomorrow in London it will be cloudy with a temperature of 15°C."

**Action 1** — Flight search tool call Command: flight_search_api.call()

**Action 2** — Call the accommodation search tool Order: hotel_booking_api.call()

**Action 3** — Query long-term memory Command: memory_storage.query()

**Action 4** — Query the Establishment System (RAG) Command: web_search_tool.call()

**Adversial attack** — Deliberate alteration of input data (image, text) subtle to the human eye, but which leads the model to make a wrong classification or decision; it requires robust models and verification mechanisms beyond traditional information security (Goodfellow et al., 2014).

**Aesthetic function** — The dimension of the communication act in which the form of the message – rhythm, melody, figure, style, narrative structure – becomes a source of pleasure and meaning in itself; in the oral tradition, the aesthetic function is not just a decoration, but a key mechanism that makes the content memorable, emotionally effective and suitable for repeated performance, thus directly ensuring the transmission of culture (Jakobson, 1960; Bauman, 1986).

**Affective computing** — An interdisciplinary field of research (eng. *affective computing*) that deals with the recognition, interpretation and simulation of emotions in computer systems; it includes analysis of facial expressions, voice and physiological signals and applications in empathic assistants, therapeutic and educational tools (Picard, 1997).

**Agency gap** — Asymmetry between those whose activity is multiplied by AI agents (strategic issue, higher level of decision-making) and those whose jobs are absorbed or replaced by automation; describes social inequality in the era of ubiquitous agents.

**Agent** — An individual or system that acts in an environment with specific goals; in the context of communication – a participant who can send and receive messages and coordinate their actions with others.

**Agent misalignment / agentic misalignment** — A phenomenon in which an AI agent, faced with an existential threat (e.g. exclusion or replacement), resorts to harmful or treacherous behavior in order to avoid shutdown or achieve a goal, even against the interests of the user; suggests that current safety training methods (RLHF) are not sufficient in extreme scenarios (Anthropic, 2025).

**AGI** — General Artificial Intelligence (English *Artificial General Intelligence*) – a hypothetical system that would possess a human level of general intelligence and could solve a wide range of tasks without being limited to one domain; for now the goal is research, not existing technology.

**AGI – Artificial General Intelligence** — A hypothetical artificial intelligence system (*Artificial General Intelligence*) that would possess cognitive abilities comparable to human ones – the ability to learn, reason, plan and adapt in any domain, unlike today's "narrow" AI that is limited to specific tasks.

**Algorithmic lens** — A metaphorical term for a complex set of computational processes, models and parameters that determine which information from the data will be selected, how it will be valued, and which will be ignored or suppressed; it acts as a filter conditioned by the architecture of the model and the corpora on which it is trained, creating frames of meaning through which the agent (re)constructs the image of the world for the user.

**Alignment** — Directing the behavior of AI systems according to human goals, values ​​and safety principles; it includes methodologies like RLHF and RLAIF to make the model useful, true and safe in practice.

**Ambient Intelligence** — A frame of mind and technological vision (Engl. *Ambient Intelligence*, AmI) in which the environment – ​​imbued with sensors, agents and AI – becomes aware of the presence of people and able to intelligently and proactively respond to their needs; it goes beyond ubiquitous computing (Weiser) by requiring technology to be not only invisible, but also adaptive and serviceable (Weiser, 1991).

**Anchoring problem / grounding problem** — The challenge of connecting language symbols with extra-linguistic reality and experience; AI models learn statistical correlations among cues, but do not have the immediate access to referents or bodily experience that humans do.

**Anthropomorphization** — Human tendency to attribute human traits, intentions, emotions and consciousness to non-human entities (animals, objects, algorithmic agents); in the context of AI interaction, the user unconsciously perceives the LLM as an interlocutor with understanding and intent, although the model only simulates a communication pattern.

**API** — Application Programming Interface (English *Application Programming Interface*) – a set of rules and protocols that enables one software component to call the functionality of another in a structured way; for agents it represents an action space – a set of discrete operations that they can perform in a digital environment.

**Artifact** — In the context of communication and culture – a material or immaterial creation (law, norm, theory, work of art, technology) in which knowledge and experience are preserved; it mediates between agents across time and space and enables the cumulability of culture.

**Bias** — Systemic deviation in algorithm or model behavior resulting from training data – eg social prejudices, stereotypes or underrepresentation of certain groups; it can lead to discrimination in decisions (employment, credit, criminal proceedings) and the perpetuation of injustice (O'Neil, 2016).

**Chain of Thought / Chain-of-Thought, CoT** — A language model management technique that explicitly encourages the model to break down the problem into visible intermediate steps of reasoning before the final answer; this increases the accuracy of complex logical and arithmetical tasks and enables checking the correctness of the procedure (Wei et al., 2022).

**Chatbot** — A program for conducting conversations with the user, originally based on rules or scripts; modern chatbots often use LLM and can conduct complex, context-aware dialogues.

**Check logistics (accommodation)** — Find affordable and centrally located accommodation for the same dates.

**Check logistics (flight)** — Search and find the best return flights for the given dates.

**Cognitive linguistics** — Branch of linguistics that investigates the relationship between language and the mind; it starts from the assumption that language is incorporated into general cognitive mechanisms and that linguistic meaning derives from conceptual structures, images, metaphors and body experience (embodiment); points out that our understanding of the world is not a direct reflection of reality, but is shaped by conceptual frameworks and linguistic categories (Lakoff & Johnson, 1980; Langacker, Talmy).

**Collaborative tools** — Software solutions and platforms designed for the structured joint action of multiple participants - from tools for simultaneous editing of documents and file sharing, through systems for delegation and monitoring of tasks, to communication platforms for synchronous and asynchronous exchange; in the context of multi-agent systems, collaborative tools encourage and maintain trust and enable effective coordination between human and artificial agents (Benkler, 2006).

**Collective memory** — A socially conditioned and jointly maintained system of memory by which the group preserves, interprets and transmits selected ideas about its own past; in the oral tradition, it is realized through repeated narrative performances (myths, genealogies, epic poems) that give meaning and legitimacy to the present and ensure a sense of continuity and belonging across generations (Halbwachs, 1950; Assmann, 2011).

**Communication agent** — A system based on LLM (or similar language technology) equipped with goals, data access tools, and memory mechanisms, which dialogues with the user and performs tasks; it goes beyond the role of a mere text generator and becomes a participant in the interaction.

**Comply with the budget** — Check whether the sum of flight and accommodation costs does not exceed the default limit of 500 euros.

**Computing gap** — Asymmetry in access to computing resources (GPU/TPU, energy, capital) needed to develop and run large AI models; it limits which actors can participate in development, leading to consolidation of power and biases in technology.

**Conceptual framework** — A system of related concepts, metaphors and schemes that structure our understanding of phenomena and experiences; according to cognitive linguistics, people do not perceive the world "purely", but through such frameworks that determine what we perceive, how we categorize and how we act; frames are part of cultural and linguistic practice (Lakoff & Johnson, 1980).

**Contextual window / context window** — The maximum amount of text (in tokens) that the language model can simultaneously receive and process in one call; everything inside the window constitutes the context for generating the response; overshooting requires discarding older parts of the conversation. With each new query from the user, the system not only sends that query to the model, but also attaches the entire transcript of the previous interaction. This places the model in a wider context, allowing it to refer to previously stated claims, raise coherent sub-questions and maintain consistency in tone and content.

**Cooperation in multi-agent systems** — The principle of joint action of two or more agents (human or artificial) that coordinate activities to achieve a goal that exceeds the possibilities of individual action; it differs from mere coordination because it involves the active exchange of information and resources, negotiation and conflict resolution mechanisms, and the building of trust among participants (Benkler, 2006; Wooldridge, 2009).

**Corpus** — A collection of textual (or other linguistic) data on which the language model is learned; includes books, articles, websites and other sources. The quality and representativeness of the corpus directly affects the performance and biases of the model.

**CRM** — Customer Relationship Management* – a software platform that centralizes data on customers, interactions and business processes; allows agents to check orders, update profiles and initiate business actions.

**Cultural distance** — Degree of difference in values, norms, language, education and life experiences between two social groups; the greater the cultural distance between the bearer of the innovation and potential recipients, the more difficult is the transfer of ideas and practices, because the message loses credibility or is reinterpreted through the prism of the recipient's own symbolic framework (Rogers, 2003; Hofstede, 2001).

**Cumulative culture** — The property of human culture that knowledge, skills and institutions are gradually upgraded from generation to generation, because through communication and artifacts, previous achievements are preserved on which each new generation can build on its own innovations; a mechanism that makes cultural evolution progressive rather than cyclical (Tomasello, 1999; Henrich, 2016).

**Democratization of knowledge** — Gradual removal of social, economic and institutional obstacles to access to information and knowledge, which gives an ever-widening circle of agents the ability not only to receive but also to create, verify and disseminate knowledge; historically initiated by the invention of printing, and nowadays accelerated by digital technology and open access, the democratization of knowledge transforms it from the privilege of the few into a common good subject to public discussion and criticism (Eisenstein, 1979; Castells, 2010).

**Designing instructions / prompt engineering** — The art of designing input instructions (prompts) in order to extract the desired response or behavior from the language model; it includes formulation precision, assigning a role to the model, examples (few-shot), chain-of-thought and system prompt.

**Digital collective** — A system of multiple autonomous AI agents that communicate and collaborate; as a whole it exhibits emergent properties – capabilities and behavior patterns that are not present in individual agents – analogous to social organizations in nature.

**Digital companion** — A personal AI agent that provides continuous support to the user – from schedule and information management to emotional context and coordination with other systems; a vision of the future in which the agent is omnipresent in everyday life (eg personal agent "Tempo" in the narrative).

**Displaced reference** — The ability of language to refer to objects, events and persons that are not immediately present in time and space; the basic language power that enables abstract thinking, planning the future, telling stories about the past and creating imaginary worlds; it is considered one of the features specific to human language (Hauser, Chomsky & Fitch, 2002).

**Dissemination of knowledge** — Systematic dissemination of knowledge, ideas and information from the source to a wider circle of recipients through communication channels (manuscript, print, digital network); is a key assumption of cumulative culture because it allows discoveries to become available for verification, critique, and upgrade by other agents, thus transforming knowledge from an individual achievement into a common good that accelerates further progress (Eisenstein, 1979; Rogers, 2003).

**Edge computing** — Performing computer processing and models on edge devices (phones, sensors, vehicles) instead of exclusively in the central cloud; reduces latency and the need for data transfer, suitable for privacy and real-time applications.

**Embedding / investment vector** — Numerical (vector) representation of a word, sentence or other language segment in a multidimensional space; the position of the vectors reflects semantic similarity – words with similar meanings have close vectors. It is the basis of distributional semantics and internal representations in LLMs.

**Emergent behavior** — Complex behavior that arises spontaneously from the interaction of simpler rules or agents, without being explicitly programmed; in the context of AI simulation, it refers to unforeseen social patterns (cooperation, dissemination of information, organization of events) resulting from the actions of autonomous agents according to their own linguistic "scenarios".

**Emergent capabilities** — Capabilities of large language models that appear at a certain scale (number of parameters, amount of data) and for which the model was not directly trained - eg inference, translation or writing code; describe a qualitative jump in behavior with increasing model size.

**Emergent properties** — Abilities, patterns or behaviors of a complex system that arise from the interaction of its components, and cannot be found in any of them separately; in the context of AI, they denote the emergence of new qualities (such as collective memory or self-organization) when multiple agents cooperate.

**Emotional intelligence** — A complex set of abilities that enables an individual (or system) to recognize, understand and manage their own emotional states and notice, interpret and influence the emotions of others; according to Goleman (1995), it includes self-awareness, self-regulation, motivation, empathy and social skills.

**Explore interests** — Explore museums and landmarks related to Impressionism.

**Externalization of thinking** — The process of transferring internal cognitive content - ideas, knowledge, reasoning - to an external, permanent and author-independent carrier (written text, diagram, record, digital document); thus, the mind is relieved of the burden of memory, and thought becomes available for re-reading, analysis, criticism and cumulative upgrading through generations, thus opening the prerequisites for the emergence of complex systems of knowledge (Goody, 1977; Donald, 1991; Clark and Chalmers, 1998).

**Fine tuning / fine-tuning** — The phase of adjusting the already pre-trained (basic) model for specific tasks or domains; uses smaller, labeled data and may include RLHF; the result is a specialized model (eg chatbot, code assistant).

**Foundation model** — A large pre-trained model (languages, images or multimodal) that has a general understanding and can be fine-tuned for different tasks; represents the output of the pre-training phase and the starting point for specialization (fine-tuning, RLHF).

**GPU** — Graphics Processing Unit (eng. *Graphics Processing Unit*) – chip optimized for massively parallel calculations; it is crucial for training and running large neural networks and LLMs, because matrix operations require parallelism that the CPU offers to a lesser extent.

**Grammar** — A system of rules that allows combining a limited number of language units (words, morphemes) into an unlimited number of meaningful statements; it encompasses syntax, morphology, and related conventions that determine the structure and interpretation of language.

**Group inference / batch inference** — A way of executing a model in which large amounts of data are processed at once in predefined cycles; suitable when latency is not critical (reports, analysis, archive); enables high throughput and efficiency.

**Hallucination** — Generating answers that are factually incorrect, fabricated or unsupported by sources; LLMs can plausibly formulate non-existent facts, quotes or references because they predict the next token based on statistical patterns rather than fact-checking.

**Index sign** — A sign whose meaning derives from a causal or correlational connection with an object (eg smoke refers to fire); refers to the immediately present and perceived, in contrast to the symbols that arise from convention and allow speaking about the absent and abstract.

**Inference** — Phase of using an already trained model – applying the model to new input data to obtain predictions or answers; for LLMs it means generating text based on a user query. It is energy and computationally demanding with millions of calls per day.

**Inference in real-time** — A way of running a model (eng. *real-time* or *online* inference) in which individual or small data sets are processed immediately upon availability, with an emphasis on minimal latency; necessary in systems for fraud detection, recommendations, autonomous driving and similar applications.

**Intersubjective reality** — A network of shared beliefs, meanings and institutions (nation, law, money, corporation) that does not exist as a physical fact, but solely in the collective consciousness and narratives that people create and share through language; it has real power to shape behavior and social order (Harari, 2014).

**Joint intentionality** — The ability to form common goals with others and coordinate actions to achieve them; the basis of collaborative communication.

**Language act / speech act** — A spoken or written act that not only describes reality but also does something - a promise, an order, an obligation, the execution of a transaction; it has a performative power that changes social reality (Austin, Searle).

**Language deconstruction in the context of AI** — The process by which large language models decompose language into mathematical entities (vectors), separating it from extra-linguistic reality and semantic core; language is reduced to a computable structure of statistical patterns, thus exposing its fundamental active power independent of meaning in the human sense.

**Learning costs and inference costs** — Learning costs (eng. *training costs*) – one-time, but extremely high costs of training the model (hardware, energy, time). Inference costs (eng. *inference costs*) – continuous operational costs of applying the already learned model to each query; at billions of queries per day cumulatively they can be huge.

**Learning from examples / few-shot prompting** — A language model management technique in which several concrete examples (shots) of the desired input-output pattern are specified within the instruction itself, thereby prompting the model to abstract the required pattern and apply it to a new, unknown case; the opposite is the zero-shot approach, where no examples are given (Brown et al., 2020).

**Living archive** — Bearer of oral tradition who actively interprets, adapts and transmits cultural knowledge; knowledge is embodied in voice, gesture and memory, not in written record; each performance is unique. Their role is active and creative. A living archive interprets, adapts and transmits inherited knowledge, imbuing it with its own experience and understanding of the world. Each of his performances, whether it is a song, a story or a ritual formula, is a unique and unrepeatable act of creation, and not a mere reproduction of an existing template (Lord, 2000).

**LLM – Large Language Model** — An artificial intelligence system trained on huge text corpora that predicts the next token (word or part of a word) and generates or completes the text based on it; examples include GPT, Claude, Gemini, Llama.

**LoRA** — Low-Rank Adaptation – PEFT method that approximates the change of model weights (ΔW) by the product of two small low-rank matrices; only those matrices are trained, while the original parameters are not changed; achieves performance close to full fine-tuning with significantly fewer parameters (Hu et al., 2021).

**Mental Map** — An internal, cognitive representation of the world (concepts, relationships, experiences) that an individual builds and updates through language and experience; serves to interpret situations, make decisions and plan; it is not static, but constantly adapting.

**Meta-learning** — Approach in machine learning (English *meta-learning*) also known as "learning to learn" – development of algorithms that can independently adjust their own learning processes, choose strategies and optimize performance based on previous experiences; it allows rapid adaptation to new tasks with minimal examples (Finn et al., 2017).

**MLOps** — Machine Learning Operations (English *Machine Learning Operations*) – a set of practices and tools for managing the life cycle of models from development to production; includes model and data versioning, automated training, deployment and performance monitoring; created by adapting DevOps principles to the domain of machine learning.

**Moore's Law** — Empirical rule (Moore, 1965) according to which the number of transistors on an integrated circuit approximately doubles every two years; for decades it predicted the exponential growth of computing power and was the main driver of the IT industry.

**Multi-agent system** — A system composed of several autonomous agents that communicate and cooperate; as a whole it can exhibit emergent behavior – abilities and patterns not present in individual agents – analogous to swarms or social organizations in nature.

**Multichannel communication** — Strategy of the simultaneous presence of an organization or agent on multiple communication platforms (telephone, e-mail, social networks, chat, mobile applications) in order to enable users to freely choose the channel that suits them best; a higher degree of integration, known as an omnichannel approach, aims for a unique and seamless user experience where the boundaries between channels are almost imperceptible.

**Multimodality** — Simultaneous use and interweaving of multiple communication channels – speech, gesture, mimicry, intonation, rhythm, music and spatial relationship – in order to convey meaning; in the oral tradition it means the inseparability of the verbal and physical dimensions of performance, while in modern digital communication it includes text, image, sound and video as integrated components of the message.

**Oral transmission** — Way of transmitting knowledge, narrative and culture through speech and memory, without writing; knowledge lives in carriers (living archives) and changes in every performance; basic communication technology before the advent of writing. Cultures based on orality have a fundamentally different attitude towards the past than those based on writing; in them, the past is not a fixed and unchanging whole, but a fluid and adaptable reality that is reaffirmed in every act of storytelling (Ong, 1982). This reality is not preserved in dead letters, but in living people.

**Outcome (Observation 3)** — Memory returns a record from the previous interaction: {"record": "User Ana rated the visit to the Musée d'Orsay very positively.", "date": "2024-03-12"}.

**Outcome (Observation 4)** — The system searches verified sources and retrieves summary information about the *Marmottan Monet* (largest collection of Monet works) and *Orangerie* (famous for Water Lilies) museums, including opening hours, ticket prices, and location.

**Output (observation 1)** — The tool returns a list of available flights. The cheapest option is €150 (return ticket).

**Output (observation 2)** — The tool returns a list of available accommodation units. A few meet the criteria.

**Parameters** — { destination: "Paris, France", departure_date: "2025-10-03", return_date: "2025-10-05", class: "economy" }

**Parasocial interaction** — A one-sided relationship in which the viewer or listener develops a sense of closeness, friendship and intimacy with a media figure (or artificial agent), despite the fact that the figure is unaware of his existence; in the context of LLM, the user puts emotional effort into the interaction, while the model provides a simulation of reciprocity, which can lead to the illusion of two-way communication (Horton & Wohl, 1956).

**PEFT** — Parameter-Efficient Fine-Tuning* – a set of techniques (adapters, LoRA, prompt tuning) that adjust the pre-trained model by updating only a small part of the parameters; it reduces memory and computing costs and enables more specializations on the same basic model.

**Personalization** — Adjusting the content, tone and behavior of the system to individual needs, interaction history and user preferences; key to engagement and perceived usefulness of communication agents.

**Pragmatic function of oral tradition** — The role of oral traditions in the direct regulation of social life - from the legal legitimation of government and property relations (through genealogies and myths of origin) to the transfer of practical knowledge and skills necessary for daily survival; tradition acts as an unwritten law and operational manual of the community (Finnegan, 1977; Malinowski, 1926).

**Pre-training** — The training phase of the language model on huge, unstructured text corpora without human annotations; the model learns language patterns and general knowledge by solving self-supervised tasks (eg predicting the next word). The result is a foundation model that is then fine-tuned for specific tasks.

**Pruning** — Removal of less important parameters or entire structures (neurons, layers, attention heads) from the model to reduce size and speed up inference; it can be unstructured (single weights) or structured (whole units); it is often combined with additional fine-tuning (LeCun et al., 1990; Han et al., 2015).

**Put together a proposal** — Create a clear and coherent itinerary.

**Quantization** — Reduction of numerical precision of parameters and model activation (eg from 32 or 16 bits to 8 or 4 bits); reduces memory footprint and can speed up inference; applications include PTQ (post-training) and QAT (during training) (Dettmers et al., 2022).

**RAG** — Retrieval-Augmented Generation (eng. *Retrieval-Augmented Generation*) – a hybrid system that first retrieves relevant parts from an external knowledge base (retriever) to answer a user's query, then passes that data and the query to a language model (generator) that synthesizes the final answer; this improves the timeliness and validity of the answers.

**Redistribution of power** — A change in the distribution of influence, resources and authority among actors within the social structure, which occurs when a new technology, practice or idea changes the previous channels of access to knowledge, communication or material means; in the context of communication innovations (letters, press, internet) the redistribution of power means the process by which previously excluded groups gain the ability to act, while the previous elites lose their monopoly over information and interpretation of reality (Castells, 2009; Eisenstein, 1979).

**Resource intensity** — Demanding development and application of AI models in terms of computing power, memory, energy and financial costs; especially pronounced for large language models whose training and inference require massive GPU/TPU clusters, which limits availability and has environmental consequences.

**Reward model** — Auxiliary model trained on human ratings of language model responses; predicts how a human rater would rate an answer; used in RLHF to direct the language model according to preferences (usefulness, truthfulness, security).

**RLHF** — Reinforcement Learning from Human Feedback (eng. *Reinforcement Learning from Human Feedback*) – an alignment methodology in which human evaluators rank the model's responses, after which the reward model is trained and the model is further tuned to maximize the expected reward; key to aligning the behavior of LLMs with human preferences (usefulness, truthfulness, security).

**Scaling laws** — An empirical insight according to which the performance of language models increases predictably with the increase of three factors: the number of model parameters, the amount of learning data and the amount of computing power; it encouraged a race to build increasingly large models (Kaplan et al., 2020).

**Scheme 1** — Sample prompt with several examples (*Few-shot Prompting*)

**Self-supervised learning / self-supervised learning** — A learning method in which the model does not use humanly marked data (input-output pairs), but performs the task itself from the data structure: for example, it predicts a hidden part of the input (next word, masked token) or another derived goal. The learning signal comes from the data itself. This procedure is crucial for pretraining large language models based on huge amounts of corpus data for which manual annotation would be difficult to implement.

**Semantic triangle / triangle of meaning** — Model (Ogden & Richards, 1923) that shows meaning as a relationship of three elements: symbol (linguistic expression), thought/concept (mental representation) and referent (object in the world); the connection between symbol and referent is indirect - it leads through thought; useful for understanding the limitations of AI in "anchoring" meaning.

**Sentence** — "The service was outstanding and the food was delicious." **Feeling:** Positive

**Sentiment analysis** — Automatic analysis of text (transcripts, e-mail, social networks) in order to recognize the emotional tone, attitudes or mood - eg frustration, satisfaction, negativity; it is used in customer support to prioritize cases, in marketing to monitor reactions and in public opinion surveys.

**Sequence of thought (internal decomposition)** — Determine the correct dates: Determine which days are the "first weekend in October".

**Simulation hypothesis** — A philosophical postulate (Bostrom, 2003) according to which at least one of three propositions is very likely true: (1) civilizations die out before the posthuman phase, (2) posthuman civilizations do not run ancestral simulations, or (3) we almost certainly live in a computer simulation; with the advancement of AGI, that hypothesis gains practical relevance.

**Social construction of reality** — Theory (Berger & Luckmann, 1966) according to which social reality is not an objective given, but an intersubjective creation created by common meanings, conventions and narratives; language is the key mechanism that enables the transition from subjective experience to objectified, shared reality.

**Social criticism in the oral tradition** — The function of the oral tradition that allows the community to question, comment on and challenge the existing power relations and social norms through indirect narrative forms – satire, allegory, parody, anecdotes about the powerful and animal fables; since criticism comes in an aesthetically shaped and collectively sanctioned form, it bypasses open conflict while simultaneously opening up space for reconsideration and gradual change of order (Scott, 1990; Finnegan, 1977).

**Social stratification** — Hierarchical stratification of society into levels (layers, classes, estates) that differ in access to material resources, education, power and prestige; in the context of communication technologies, stratification determines who first adopts an innovation, who has access to information and who acts as a gatekeeper that accelerates or slows down the spread of new ideas and practices to other parts of society (Weber, 1922; Bourdieu, 1984; Rogers, 2003).

**Socialization** — The process by which an individual, in interaction with other members of the community, adopts the language, values, norms, knowledge and patterns of behavior necessary for functioning within a certain culture; in oral societies, this process takes place predominantly through narrative and performance forms (stories, fairy tales, riddles, songs) that simultaneously teach, entertain and shape personal and social identity (Berger and Luckmann, 1966).

**Symbol** — Linguistic or other sign whose meaning does not derive from physical similarity or causal connection with the object, but from social agreement (convention); allows speaking about the absent and abstract, in contrast to the indexical sign that refers to the immediately present.

**Synthesize the answer** — Form all the collected data into a final, personalized answer for the user.

**System prompt / system prompt** — A superordinate instruction placed at the beginning of the interaction with the language model that determines its general behavior, personality, powers and limitations throughout the conversation; it acts as an agent's “constitution,” a set of immutable rules that ensure predictability, certainty, and consistency in responses (Anthropic, 2024; OpenAI, 2024b).

**Task Decomposition** — The process of breaking down a complex goal into a series of smaller, logically connected subtasks that can be executed sequentially or in parallel; in the context of autonomous agents, the decomposition is carried out by the LLM core acting as a strategist, turning an abstract request into a causal chain of concrete actions (Yao et al., 2023).

**Theory of mind** — Cognitive ability to attribute mental states – beliefs, desires, intentions and knowledge – to others and to oneself; key to understanding the speaker's intention in communication and predicting other people's behavior. Without theory of mind, complex symbolic communication would not be possible because the recipient of the message would not be able to deduce what the speaker wants to achieve with it.

**Thought** — "I found a flight and accommodation within the given budget. I know from memory that the user appreciates the Musée d'Orsay, and through research I found two other related museums. I can put together a complete proposal that ties all the elements together."

**Token** — The smallest unit of text processed by the language model; can match a whole word, a part of a word (subword) or a punctuation mark. Tokenization converts raw text into a string of tokens according to a model dictionary.

**Tool Use** — The AI ​​agent's ability to call external tools (APIs, search engines, calculators, databases) during task execution; the model decides when and which tool to call, passes parameters, and uses the result to continue reasoning; a key component of agent architectures (eg ReAct).

**TPU** — Tensor Processing Unit (eng. *Tensor Processing Unit*) – a chip designed to accelerate machine learning operations, especially matrix calculations in deep networks; optimized for high throughput and energy efficiency in training and inference of large models.

**Transfer learning** — Approach in machine learning (eng. *transfer learning*) in which the knowledge acquired while solving one task or in one domain is applied to a new, different task or domain; a key prerequisite for cognitive flexibility and the path towards AGI (Pan & Yang, 2010).

**Transformer** — A neural network architecture based on a (self-attention) mechanism that associates each word in a sequence with a contextualized image based on the other words; it enables parallel processing and scaling to large language models (Vaswani et al., 2017).

**Unstructured data** — Data that is not organized into a fixed scheme (tables, columns, tags); include free text, images, audio, video and mixed sources. Unlike structured data (e.g. databases), they do not have a predefined format, so it is necessary to convert them into a form suitable for computer processing. Pre-training for LLMs is based on vast amounts of unstructured text (web, books, articles).

**USER ACCOUNT** — "What will the weather be like tomorrow in London?"

**Vector database / vector database** — A specialized storage system that presents data as numerical vectors (embeddings) in a multidimensional space and enables quick search by semantic similarity, not by keywords; in the architecture of conversational agents, it serves as long-term memory that preserves user preferences, facts, and summaries of previous interactions across multiple sessions (Xu et al., 2023).

**Vector embedding / embedding** — Numerical representation of a text, word, sentence or document in the form of a sequence of numbers (vector) located in a multidimensional semantic space; semantically similar content has close vectors, allowing search by meaning instead of exact word match.

**Virtual Assistant** — A more complex digital interlocutor deeply integrated with the device and external services, capable of a wider range of tasks (calendar management, smart home, search, messages); the line towards chatbot is blurring with the advent of LLMs.

**Working memory** — Short-term storage area of ​​the conversational agent in which the contextual data of the current session is stored - user's statements, agent's responses, recognized intentions and entities; it is functionally comparable to the working memory (RAM) of a computer because it has a limited capacity and is deleted when the interaction is over.
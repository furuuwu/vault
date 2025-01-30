# LangChain (GPT)

## intro

**LangChain** is a framework designed for building applications powered by **large language models (LLMs)** like OpenAI's GPT. LangChain is specifically designed to assist in the construction of applications that involve **LLM integration**, **data processing**, and **tool usage**. It simplifies interacting with LLMs by offering various components and tools for creating sophisticated and modular pipelines.

### **Main Concepts of LangChain**

1. **Chains**:  
   Chains are a series of calls to language models or other services. They allow you to create more complex interactions by linking together a sequence of steps that operate on the input data.

   **Example:**

   ```python
   from langchain.chains import LLMChain
   from langchain.prompts import PromptTemplate
   from langchain.llms import OpenAI

   # Define a simple prompt template
   prompt = PromptTemplate(input_variables=["name"], template="Hello, {name}!")

   # Initialize the LLM (in this case, OpenAI GPT-3)
   llm = OpenAI(temperature=0.7)

   # Create a chain from the prompt template and LLM
   chain = LLMChain(llm=llm, prompt=prompt)

   # Run the chain
   result = chain.run(name="Alice")
   print(result)  # Output: Hello, Alice!
   ```

   In this example, a simple **LLMChain** is defined that generates a greeting using the OpenAI model. The `PromptTemplate` is used to structure the input, and the chain runs the model.

2. **Prompt Templates**:  
   Prompt Templates allow you to define reusable prompt structures that can dynamically insert data or variables. This is helpful for standardizing prompt structures in larger applications.

   **Example:**

   ```python
   from langchain.prompts import PromptTemplate

   # Define a prompt template with placeholders
   prompt = PromptTemplate(input_variables=["question"], template="Answer the following question: {question}")

   # Use the template to fill in a dynamic value
   question = prompt.format(question="What is the capital of France?")
   print(question)  # Output: Answer the following question: What is the capital of France?
   ```

3. **Memory**:  
   Memory in LangChain allows you to store information between steps or sessions. This is useful for creating applications that require context persistence across user interactions, like chatbots or conversational agents.

   **Example:**

   ```python
   from langchain.memory import ConversationBufferMemory
   from langchain.chains import ConversationChain
   from langchain.llms import OpenAI

   # Initialize memory and language model
   memory = ConversationBufferMemory()
   llm = OpenAI()

   # Initialize the conversation chain with memory
   conversation = ConversationChain(memory=memory, llm=llm)

   # Run the conversation
   response_1 = conversation.predict(input="Hello, who are you?")
   print(response_1)  # Output: response based on LLM
   response_2 = conversation.predict(input="What is your name?")
   print(response_2)  # Output: response based on previous conversation context
   ```

   Here, a **ConversationBufferMemory** is used to keep track of the conversation, so the LLM can respond based on the context of previous interactions.

4. **Agents**:  
   Agents in LangChain allow you to create models that can perform actions based on a series of decisions or conditions. They can use LLMs to interpret the context, choose actions, and interact with external tools.

   **Example:**

   ```python
   from langchain.agents import initialize_agent, Tool
   from langchain.agents import AgentType
   from langchain.llms import OpenAI

   # Initialize the language model
   llm = OpenAI()

   # Define a simple tool
   def say_hello(name):
       return f"Hello, {name}!"

   tool = Tool(
       name="SayHello",
       func=say_hello,
       description="Say hello to the user."
   )

   # Create an agent that uses the tool
   agent = initialize_agent([tool], llm, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

   # Run the agent with an input that triggers the tool
   result = agent.run("Say hello to Bob.")
   print(result)  # Output: Hello, Bob!
   ```

   In this example, an agent uses a simple function (`say_hello`) as a tool to generate responses based on the input it receives.

5. **Tooling**:  
   LangChain enables integration with various **external tools**, such as APIs or databases. These tools can be invoked by the agent or chain to extend the capabilities of the language model.

   **Example:**

   ```python
   from langchain.tools import Tool
   from langchain.llms import OpenAI

   # Tool that fetches the current time
   def get_current_time():
       from datetime import datetime
       return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

   tool = Tool(
       name="CurrentTime",
       func=get_current_time,
       description="Fetch the current time."
   )

   llm = OpenAI()

   # Using the tool within a chain
   result = tool.run([])
   print(result)  # Output: current time
   ```

6. **Documents and Indexes**:  
   LangChain allows you to store, retrieve, and process documents. You can create document stores or indexes to work with unstructured data.

   **Example:**

   ```python
   from langchain.document_loaders import TextLoader
   from langchain.embeddings import OpenAIEmbeddings
   from langchain.vectorstores import FAISS

   # Load documents
   loader = TextLoader("my_document.txt")
   documents = loader.load()

   # Convert documents into embeddings
   embeddings = OpenAIEmbeddings()

   # Store documents in FAISS vector store
   vector_store = FAISS.from_documents(documents, embeddings)

   # Retrieve similar documents
   query = "What is LangChain?"
   results = vector_store.similarity_search(query)
   print(results)
   ```

---

### **Alternatives to LangChain**

While LangChain is great for building language model-driven applications, there are several alternatives in the space that offer similar functionality or provide unique features. Here are some prominent alternatives:

1. **LlamaIndex (formerly GPT Index)**:
   - **Use Case**: Designed to help with document retrieval tasks and use cases involving LLMs working with unstructured data.
   - **Features**: Efficient document indexing and retrieval, integrates with various data stores and APIs.
   - **Example Use Case**: Create an application that searches through a large collection of documents or knowledge base using LLMs.

   **Example**:

   ```python
   from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

   # Load documents
   documents = SimpleDirectoryReader('path/to/docs').load_data()

   # Create index
   index = GPTSimpleVectorIndex.from_documents(documents)

   # Query the index
   response = index.query("What is LangChain?")
   print(response)
   ```

2. **Haystack**:
   - **Use Case**: Haystack is a framework designed for building **search and question-answering systems** using transformer-based models.
   - **Features**: Supports document search, QA pipelines, and retrieval-augmented generation (RAG).
   - **Example Use Case**: Build a knowledge base search engine with advanced NLP capabilities.

   **Example**:

   ```python
   from haystack.nodes import FARMReader, TransformerReader
   from haystack.pipelines import ExtractiveQAPipeline
   from haystack.utils import launch_tensorboard

   # Load reader and retriever models
   reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2")

   # Pipeline for extractive question answering
   pipe = ExtractiveQAPipeline(reader)

   # Run the pipeline
   result = pipe.run(query="What is LangChain?", top_k_retriever=10, top_k_reader=5)
   print(result)
   ```

3. **GPT-3 (directly using OpenAI API)**:
   - **Use Case**: For simpler applications, directly interacting with OpenAI’s GPT-3 via API calls without an overarching framework.
   - **Features**: Direct interaction with GPT-3 models, customizable prompts and interactions.
   - **Example Use Case**: Building a chatbot or simple data-driven language application using OpenAI's API.

   **Example**:

   ```python
   import openai

   openai.api_key = 'your-api-key'

   response = openai.Completion.create(
       engine="text-davinci-003",
       prompt="Tell me about LangChain.",
       max_tokens=100
   )

   print(response.choices[0].text.strip())
   ```

4. **Rasa**:
   - **Use Case**: Focuses on building conversational AI and chatbots. Rasa can be used for natural language understanding (NLU) and dialogue management.
   - **Features**: Customizable workflows, dialog flow, integrations with various tools and databases.
   - **Example Use Case**: Create an AI assistant that uses natural language processing to interact with users.

   **Example**:  
   Refer to the [Rasa documentation](https://rasa.com/docs/) for detailed example code on building conversational bots.

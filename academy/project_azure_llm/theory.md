# Azure OpenAI - RAG

This is very similar to this

* [Intro and demo to RAG with Azure OpenAI](https://www.youtube.com/watch?v=vjbNSMswN2I)

![alt text](img/{B88DF91C-14C1-4E91-B5EB-F696B4631F96}.png)

![alt text](img/{5910CEE8-CD52-41E6-9736-CDE1BD2D24B0}.png)

![alt text](img/{526B052C-863D-4163-B641-E293F13A073D}.png)

![alt text](img/{4262DF49-1202-4742-956D-8A0E1DCCBE42}.png)

## Azure AI Services

This now groups the previously named `Cognitive Services` and `AppliedAI Services`

I want to use some of these services. In particular, these ones

* Azure OpenAI
* Document Intelligence
* AI Search

To make that easier to manage, I want to create an instance of Azure AI Services

![alt text](img/{CB5F3479-3E84-420C-AE38-B2B966853A44}.png)

I want to create one of these

![alt text](img/{7BB104A0-3701-4C4B-9016-5BBB68F654EB}.png)

As it says in the description, this service is just a bundle.
> Get access to Azure OpenAI, Speech, Vision, Language, and Translator Azure AI services with a single API key. Quickly connect services together to achieve more insights into your content and easily integrate with other services.

![alt text](img/{1705EBB1-149C-498E-B136-76042F1193A1}.png)

![alt text](img/{1F1C3D9D-61EA-47C3-892C-79CBEEC26080}.png)

After the resource is created, notice the link to Azure AI Foundry - <https://ai.azure.com/>, which will be used later.

As you can see, it lists all the API keys for different services, in different tabs, should you need them

![alt text](img/{C0231888-D660-4A42-B249-0490B02F3DE4}.png)

![alt text](img/{CEBB02F8-45F9-40A8-B7D9-C6650CACAF78}.png)

You can also create the Azure Ai Services instance (and any resource for that matter) through the marketplace, but, confusingly, you can find services with the same name...

![alt text](img/{2A49B52F-88F7-447E-82B2-5E75048EBB1E}.png)

![alt text](img/{AEE1AD07-0CA6-4A46-AB28-389C7995DADB}.png)

### Document intelligence

Turn documents into usable data at a fraction of the time and cost.

![alt text](img/{D2F6CDC9-3CF6-4CF6-BBE3-E00D98D9C9B7}.png)

### Azure OpenAI account

Perform a wide variety of natural language tasks.

### AI Search

Bring AI-powered cloud search to your mobile and web apps.

## Azure AI Foundry

<https://ai.azure.com/>

This was previously called `Azure AI Studio`

![alt text](img/{B04AFA57-0043-411E-A0E5-E487C25D526A}.png)

this is where you choose a llm to deploy

![alt text](img/{88820A91-F977-433E-8DA0-AD6CC779508D}.png)

![alt text](img/{6121F834-55A5-4432-BD42-A4D5A94A225D}.png)

![alt text](img/{01CF5C72-923B-4A90-9E1E-B6D6AABFF0B5}.png)

![alt text](img/{F2C63CFA-05AD-4EEF-8C12-57D51997C460}.png)

you can change this later (update the deployment)

![alt text](img/{2BF29279-D376-456D-AB83-0368DC1600E0}.png)

[Microsoft Azure - Introducing new deployment and cost management solutions for Azure](https://www.youtube.com/watch?v=SHB-qKxjooM)

the model is acessible via an api endpoint

![alt text](img/{AA5698BF-AAE6-4B3D-9DA3-C0EFE1A49A5B}.png)

you also need an additional model to create the vector embeddings

![alt text](img/{6F14F137-2807-4675-9AA3-CD96AA96075F}.png)

## Other

* [azure ai foundry templates](https://azure.github.io/ai-app-templates/)

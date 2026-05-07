---
title: "Multi-modal Image Search with Embeddings & Vector DBs"
source: "https://medium.com/@tenyks_blogger/multi-modal-image-search-with-embeddings-vector-dbs-cee61c70a88a"
author:
  - "[[The Tenyks Blogger]]"
published: 2023-08-28
created: 2026-05-07
description: "More"
tags:
  - "clippings"
---
*Use embeddings with Vector DBs to perform multi-modal search on images.*

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*GfSaPsZg5qKRPD5mHzWGng.png)

Embeddings are a powerful way to represent and capture the semantic meaning and relationships between data points in a vector space. While word embeddings in NLP have become very popular, researchers have developed embedding techniques for images, audio, and other modalities.

In this article, we will explore how we can leverage image embeddings to enable multi-modal search over image datasets. This kind of search takes advantage of a vector database, see our article on Vector DB [here](https://medium.com/@tenyks_blogger/vector-databases-unlock-the-potential-of-your-data-5bd4950bd72), a special kind of database optimized for fast retrieval over high-dimensional embedding vectors. By indexing image embeddings in a vector database, we can enable semantic search over images — using text queries and image queries.

Lastly, we will showcase how the Tenyks platform employs this approach to enable *image search*, given a query based on text, images, or cropped-out objects.

## Table of Contents

1. Foundations
2. Search pipeline
3. Multi-modal image search in action
4. Summary

## 1\. Foundations

We begin by defining *three* of the main building blocks to understand multi-modal search:

### Embeddings

Embeddings encode a *single data modality*, like words, images, audio, etc into a vector space. For example, word embeddings encode words into a semantic vector space. Image embeddings encode images into a visual vector space. These embeddings represent the meaning and relationships between a *single type* of data.

### Multi-modal embeddings

Multi-modal embeddings encode and relate *multiple* different data modalities into a shared embedding space. As a result, we can represent high-level, semantic relationships and connections across modalities.

The concept of embeddings for a single data type is not novel; clustering CNN image embeddings to find visually similar images has been used for years. New approaches that leverage massive internet data have enabled a new frontier: aligning images and text in a shared vector space.

Powerful models trained on huge datasets have learned a common semantic meaning across modalities (see Figure 1). Images and captions, objects and attributes, even videos and transcripts can now be represented using the same high-level features. Searching with a photo to find related products or news stories is the exciting potential of multi-modal embeddings.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*bOy1mc4v5QhVbFtQg5q90g.png)

Figure 1. Segment Anything \[1\] leverages multi-modal embeddings

The real innovation is converting between data types within one model. A system skilled with both pictures and words can translate one into the other, use them together in a job, even create new data types by merging current ones in vector space.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*IUAfsDshnOtYcOgcmiOePg.png)

Table 1. Comparing models capable of generating multi-modal embeddings

CLIP \[2\] is a model developed by OpenAI that can learn joint representations of images and their associated textual descriptions. By training on large-scale datasets containing images and their corresponding captions, CLIP learns to embed images and texts into a shared latent space. Table 1 shows CLIP’s main characteristics next to other similar models.

🤓 If interested, Hugging Face has an available implementation of these models: [CLIP](https://huggingface.co/docs/transformers/model_doc/clip), [VisualBert](https://huggingface.co/docs/transformers/model_doc/visual_bert), and [LXMERT](https://huggingface.co/docs/transformers/model_doc/lxmert).

### VectorDBs

A **vector database** is a special-purpose database to store and manage embeddings. It’s optimized for similarity searching in applications such as image search, recommender systems, and many more.

⚡ Dive deeper into what a **Vector DB** is in our [article](https://medium.com/@tenyks_blogger/vector-databases-unlock-the-potential-of-your-data-5bd4950bd72) on that topic.

## 2\. Search pipeline

Multi-modal embeddings enable natural language search of non-text data. Without manual annotation, a system can understand concepts and semantic relationships *across modalities*. For instance, querying an image dataset for “taxis” will retrieve *only* taxi photos, allowing rapid model analysis for that category without extra work.

### Why multi-modal search for model debugging

This approach to search powers essential capabilities like model debugging, performance evaluation on specific subsets, and model interpretability. Searching visual data with text illuminates how the model comprehends language and images. The system response suggests captions, labels or attributes it associates with different objects, scenes or attributes, revealing potential model biases or blind spots.

Most model issues emerge at the frontier— for niche cases, minorities, edge scenarios. But evaluating model behaviour for every data corner is infeasible. Multi-modal search provides a mechanism for broad, flexible interrogation of how a model functions, what it captures accurately or omits for different modalities. This meta-analysis, enabled by joint text and image understanding in vector space, is crucial to build trust and safety into AI systems.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*yZYeqPt4dDGGScsQ6AzZkg.png)

Figure 2. More detailed view of search pipeline in the Tenyks platform

### Tenyks search pipeline

At Tenyks we take advantage of embeddings to enable multi-modal search. Figure 2 shows at a high-level Tenyk’s multi-modal search pipeline.

1. After you upload a dataset, we use a number of embedding models (e.g. CLIP), depending on the use-case, to extract the embedding of each image in your dataset.
2. These embeddings are stored (i.e. indexed) in a vector database, which is responsible of handling and managing all the operations related to the embeddings (i.e. create or edit records).

Both, 1 and 2 comprise the **indexing stage** of the search pipeline. All the remaining steps correspond to the **search stage**.

3\. A user in the Tenyks platform inputs a query by:

- *Image*: simply selects one of the images in the dataset.
- *Text*: a phrase such as: “find images of cars waiting for pedestrians to cross the street”.
- *Cropped-out object*: this corresponds to bounding box objects in a particular image.

4\. The embedding model (e.g. CLIP) takes the query as input, and yields its embedding as output.

5\. The vector database receives the embedding (i.e the query), applies a similarity search algorithm (e.g. cosine similarity) to find the most similar indexed embeddings to the given query.

6\. The nearest neighbour results from the vector database are organized based on relevance/similarity score, where the top ranked images are returned as the search results for the given query.

7\. The user can see on the Tenyks platform the result of her/his query.

## 3\. Multi-modal image search in action

At [Tenyks](https://www.tenyks.ai/), we perform lightning-fast image searches across large volumes of vector data.

Here’s an example of a use case of multi-modal search in action. Using the [BDD](https://bair.berkeley.edu/blog/2018/05/30/bdd/) dataset, a driving dataset, we are interested in searching for images based on three different modalities.

### Text search

We can start by finding images of taxis by querying using the text: “Taxis”. As shown in Figure 3, after typing the desired text query, we obtain a set of images, each of which contains at least one taxi.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*JUswoxrrxFEkFjRxo3A2BA.gif)

Figure 3. Searching for images using text

### Image search

Next, we can also provide a given image as input. Figure 4 demonstrates how, after selecting an image containing crosswalks, the search engine retrieves a set of images that also displays crosswalks.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Kwy0VuYZem8fzUGfZ7Hk4g.gif)

Figure 4. Given an image, we can use multi-modal search to retrieve similar images

### Object-level search

Lastly, suppose you are interested in conducting a more granular search. Instead of searching by selecting a whole image, we can do object-level search. Figure 5 illustrates how, by intentionally selecting an object from the *Bus* class, the search results contain images with objects of the class *Bus*.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*zb7etEeb9-m9Kb-TL0c5YQ.gif)

Figure 5. Multi-modal search in the Tenyks platform given a cropped-out object (i.e. Bus class)

## 4\. Summary

Using a vector database optimized for similarity search over embeddings enables the Tenyks platform to do multi-modal image search at very large scale, with tens of thousands of images indexed and queries taking just milliseconds. The end result is a search experience where the results are ranked based on semantic visual similarity rather than just keywords or metadata.

### References

*\[*[*1*](https://arxiv.org/pdf/2304.02643.pdf)*\] Segment Anything*

*\[*[*2*](https://arxiv.org/abs/2103.00020)*\] Learning Transferable Visual Models From Natural Language Supervision*

**Authors**: Jose Gabriel Islas Montero, Dmitry Kazhdan

*If you would like to know more about* ***Tenyks****, sign up for a* [*sandbox account*](https://tenyks.docsend.com/view/cyzf9j64wytwgtaj)*.*

![Tenyks logo.](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*cz2g3N9T23NJC8FqupDOJQ.png)

Tenyks logo.
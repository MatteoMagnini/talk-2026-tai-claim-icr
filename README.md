# Symbolic Knowledge Extraction and Injection: Theory and Methods

Artificial intelligence has traditionally been approached from two complementary perspectives: symbolic AI, which relies on structured, formal representations of knowledge, and sub-symbolic AI, which leverages data-driven learning methods such as deep neural networks.
While symbolic approaches offer interpretability and logical reasoning, sub-symbolic methods provide flexibility and scalability in processing large datasets. To fully leverage their respective strengths, a growing body of research explores techniques for integrating these paradigms.

This talk aims to provide a structured overview of how symbolic and sub-symbolic AI can be connected.
We will begin by clarifying the distinction between symbolic and sub-symbolic representations, introducing key symbolic formalisms, and recalling fundamental machine learning concepts.
We will then define Symbolic Knowledge Extraction (SKE), which seeks to distill structured knowledge from sub-symbolic models, and Symbolic Knowledge Injection (SKI), which incorporates symbolic knowledge into learning processes.
A taxonomy of SKE methods will be presented, followed by an overview of SKI techniques, along with concrete examples of algorithms that instantiate these approaches.

Finally, we will discuss applications that benefit from combining symbolic and sub-symbolic methods, as well as potential directions for future research.

## Background

1. AI map: symbolic vs sub-symbolic
3. Examples of symbolic formalisms
4. Examples of ML methods
5. Symbolic vs. distributed representations, interpretations
6. Differences and complementarities
7. Why one may want to connect symbolic and sub-symbolic AI

8. Brief overview of how statistical learning works
9. Brief overview of how NN training works

## SKE

1. Definition and motivation (explainability)
2. Concept (trivial I/O example to give intuition)
3. Cart example, overview
4. Cart example, code
5. Taxonomy of methods
6. Discussion (notable remarks, limitations, future research activities)

## SKI

1. Definition and motivation (trustworthy AI)
2. Concept (trivial I/O example to give intuition)
3. Overivew: semantic loss function example + KINS example
4. Code: bare semantic loss function in torch, stressing fuzzification
5. Taxonomy of methods
6. Discussion (notable remarks, limitations, future research activities)
7. Discussion on the impact of LLM onto the SKI research line

## Wrapping up

- Conclusions

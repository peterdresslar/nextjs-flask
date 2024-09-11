# Demonstration Project

This is a demonstration project using an example project from the Vercel python examples at [https://github.com/vercel/examples](https://github.com/vercel/examples).

What we want to demonstrate is "pair programming" in Cursor between me (@peterdresslar) and an AI chatbot. Our `main` branch will have the base example.

In our branches, we'll use different AI engines to accomplish more or less the same tweak to the codebase--we want to alter the example to actually demonstrate communication between the Next React app and the Flask API. This is a simple example, but does involve a little bit of knowledge about the environments that extends well beyond pure TS/Python code. 

We'll use a nonstandard (as of now!) file called `chats.txt` in the root to capture some chat messages.

## Branches

This project has multiple branches, each demonstrating different features or modifications:

- [main](../../tree/main): The base example of the Next.js and Flask integration.
- [claude-branch](../../tree/claude-branch): Implements communication between Next.js and Flask using Claude AI assistance.
- [gpt4-branch](../../tree/gpt4-branch): Implements communication between Next.js and Flask using GPT-4 AI assistance.
- [cursor-branch](../../tree/cursor-branch): Implements communication between Next.js and Flask using Cursor AI (A modified GPT-4o mini?)assistance.
- [deploy-me-pg](../../tree/deploy-me-pg): With an example postgres (Neon) database integration. Requires a `.env` file with a `POSTGRES_URL` environment variable. `.env.example` is provided as an example.

### Chats.txt Differences

Each branch contains a `chats.txt` file that captures chat messages. The contents of these files differ based on the specific AI engine used and the interactions that took place during the implementation. Be sure to check the `chats.txt` file in each branch to see the unique messages and problem-solving approaches used by different AI assistants.

---

<p align="center">
  <a href="https://nextjs-flask-starter.vercel.app/">
    <img src="https://assets.vercel.com/image/upload/v1588805858/repositories/vercel/logo.png" height="96">
    <h3 align="center">Next.js Flask Starter</h3>
  </a>
</p>

<p align="center">Simple Next.js boilerplate that uses <a href="https://flask.palletsprojects.com/">Flask</a> as the API backend.</p>

<br/>

## Introduction

This is a hybrid Next.js + Python app that uses Next.js as the frontend and Flask as the API backend. One great use case of this is to write Next.js apps that use Python AI libraries on the backend.

## How It Works

The Python/Flask server is mapped into to Next.js app under `/api/`.

This is implemented using [`next.config.js` rewrites](https://github.com/vercel/examples/blob/main/python/nextjs-flask/next.config.js) to map any request to `/api/:path*` to the Flask API, which is hosted in the `/api` folder.

On localhost, the rewrite will be made to the `127.0.0.1:5328` port, which is where the Flask server is running.

In production, the Flask server is hosted as [Python serverless functions](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python) on Vercel.

## Demo

https://nextjs-flask-starter.vercel.app/

## Deploy Your Own

You can clone & deploy it to Vercel with one click:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?demo-title=Next.js%20Flask%20Starter&demo-description=Simple%20Next.js%20boilerplate%20that%20uses%20Flask%20as%20the%20API%20backend.&demo-url=https%3A%2F%2Fnextjs-flask-starter.vercel.app%2F&demo-image=%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F795TzKM3irWu6KBCUPpPz%2F44e0c6622097b1eea9b48f732bf75d08%2FCleanShot_2023-05-23_at_12.02.15.png&project-name=Next.js%20Flask%20Starter&repository-name=nextjs-flask-starter&repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Fnextjs-flask&from=vercel-examples-repo)

## Developing Locally

You can clone & create this repo with the following command

```bash
npx create-next-app nextjs-flask --example "https://github.com/vercel/examples/tree/main/python/nextjs-flask"
```

## Getting Started

First, install the dependencies:

```bash
npm install
# or
yarn
# or
pnpm install
```

Then, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

The Flask server will be running on [http://127.0.0.1:5328](http://127.0.0.1:5328) – feel free to change the port in `package.json` (you'll also need to update it in `next.config.js`).

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.
- [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/) - learn about Flask features and API.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

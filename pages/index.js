// pages/index.js

import Head from 'next/head';
import ChatInterface from '../components/ChatInterface';

export default function Home() {
  return (
    <div>
      <Head>
        <title>Data Analysis Chat</title>
        <meta name="description" content="Data Analysis Chat Interface" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main>
        <ChatInterface />
      </main>

      <footer>
        {/* Footer content */}
      </footer>
    </div>
  );
}

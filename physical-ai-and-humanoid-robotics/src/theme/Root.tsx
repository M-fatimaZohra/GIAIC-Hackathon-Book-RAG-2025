import React, { useState } from 'react';
import Root from '@theme-original/Root';
import ChatbotButton from '@site/src/components/ChatbotButton';
import ChatbotWindow from '@site/src/components/ChatbotWindow';

export default function RootWrapper(props) {
  const [isChatOpen, setIsChatOpen] = useState(false);

  const handleToggleChat = () => {
    setIsChatOpen((prev) => !prev);
  };

  return (
    <>
      <Root {...props} />
      <ChatbotButton onToggle={handleToggleChat} isOpen={isChatOpen} />
      <ChatbotWindow isOpen={isChatOpen} />
    </>
  );
}
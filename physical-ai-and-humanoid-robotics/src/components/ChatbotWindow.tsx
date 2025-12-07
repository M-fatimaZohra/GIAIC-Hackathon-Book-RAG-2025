import React, { useState, useRef } from 'react';
import styles from './ChatbotWindow.module.css';

interface ChatbotWindowProps {
  isOpen: boolean;
}

const ChatbotWindow: React.FC<ChatbotWindowProps> = ({ isOpen }) => {
  const [messages, setMessages] = useState<{ text: string; sender: 'user' | 'bot' }[]>([{ text: 'Hello! How can I help you today?', sender: 'bot' }]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [timeoutMessage, setTimeoutMessage] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const timeoutRef = useRef<NodeJS.Timeout | null>(null);

  const handleSendMessage = async () => {
    if (input.trim() && !isLoading) {
      const userMessage = { text: input, sender: 'user' as const };
      setMessages((prevMessages) => [...prevMessages, userMessage]);
      setInput('');
      setIsLoading(true);
      setTimeoutMessage(null);
      setError(null);

      // Set a timeout for the "taking longer" message
      timeoutRef.current = setTimeout(() => {
        setTimeoutMessage('Sorry, this is taking longer than expected. Please wait, or try again later.');
      }, 5000); // 5 seconds for demonstration (was 5 minutes)

      try {
        // Simulate network delay
        await new Promise((resolve) => setTimeout(resolve, 2000)); // 2 seconds delay

        // Simulate an error randomly (e.g., 20% chance)
        if (Math.random() < 0.2) {
          throw new Error('Network error or unexpected issue.');
        }

        const botResponse = { text: `This is a mock response to: "${input}"`, sender: 'bot' as const };
        setMessages((prevMessages) => [...prevMessages, botResponse]);
      } catch (err) {
        console.error('Chatbot error:', err);
        setError('Could not get a response. Please check your connection and try again.');
      } finally {
        setIsLoading(false);
        if (timeoutRef.current) {
          clearTimeout(timeoutRef.current);
          timeoutRef.current = null;
        }
      }
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      handleSendMessage();
    }
  };

  if (!isOpen) {
    return null;
  }

  return (
    <div className={styles.chatbotWindow}>
      <div className={styles.chatHeader}>Chatbot</div>
      <div className={styles.chatMessages}>
        {messages.map((message, index) => (
          <p key={index} className={message.sender === 'user' ? styles.userMessage : styles.botMessage}>
            {message.text}
          </p>
        ))}
        {isLoading && <p className={styles.loadingMessage}>Bot is thinking...</p>}
        {timeoutMessage && <p className={styles.timeoutMessage}>{timeoutMessage}</p>}
        {error && <p className={styles.errorMessage}>{error}</p>}
      </div>
      <div className={styles.chatInputArea}>
        <input
          type="text"
          placeholder="Type your message..."
          className={styles.chatInput}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={handleKeyPress}
          disabled={isLoading}
        />
        <button className={styles.sendButton} onClick={handleSendMessage} disabled={isLoading}>
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatbotWindow;
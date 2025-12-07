import React from 'react';
import styles from './ChatbotButton.module.css'; // We will create this CSS module later

interface ChatbotButtonProps {
  onToggle: () => void;
  isOpen: boolean;
}

const ChatbotButton: React.FC<ChatbotButtonProps> = ({ onToggle, isOpen }) => {
  return (
    <button className={styles.chatbotButton} onClick={onToggle}>
      {isOpen ? 'Close Chat' : 'Open Chat'}
    </button>
  );
};

export default ChatbotButton;
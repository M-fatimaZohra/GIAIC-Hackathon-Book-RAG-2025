import React from 'react';
import Link from '@docusaurus/Link';
import styles from './NavbarPlaceholderButton.module.css';

type NavbarPlaceholderButtonProps = {
  label: string;
  backgroundColor: string;
};

export default function NavbarPlaceholderButton({ label, backgroundColor }: NavbarPlaceholderButtonProps): JSX.Element {
  const handleClick = () => {
    alert('Coming soon');
  };

  return (
    <button
      className={styles.navbarPlaceholderButton}
      style={{ backgroundColor: backgroundColor }}
      onClick={handleClick}>
      {label}
    </button>
  );
}

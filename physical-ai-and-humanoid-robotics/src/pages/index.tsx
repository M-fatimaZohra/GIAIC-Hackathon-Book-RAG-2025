import React from 'react';
import clsx from 'clsx';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import styles from './index.module.css';

type FeatureItem = {
  title: string;
  description: string;
  link: string;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Course Details',
    link: '/docs/course-details',
    description: 'Learn about the course structure, objectives, and prerequisites for Physical AI & Humanoid Robotics.',
  },
  {
    title: 'Module 1: The Robotic Nervous System (ROS 2)',
    link: '/docs/module1-overview',
    description: 'Explore the fundamentals of ROS 2 for building robust robotic applications.',
  },
  {
    title: 'Module 2: The Digital Twin (Gazebo & Unity)',
    link: '/docs/module2-overview',
    description: 'Learn to create and simulate virtual robots in Gazebo and Unity environments.',
  },
  {
    title: 'Module 3: The AI-Robot Brain (NVIDIA Isaac)',
    link: '/docs/module3-overview',
    description: 'Dive into NVIDIA Isaac platform for advanced AI and robotics simulations.',
  },
  {
    title: 'Module 4: Vision-Language-Action (VLA)',
    link: '/docs/module4-overview',
    description: 'Understand how to integrate vision, language, and action for intelligent robot behavior.',
  },
  {
    title: 'Weekly Breakdown',
    link: '/docs/weekly-breakdown',
    description: 'See the detailed week-by-week schedule, covering lectures, labs, and project milestones.',
  },
  {
    title: 'Assessments',
    link: '/docs/assessments',
    description: 'Understand the course assessment structure, including lab assignments, midterm, and capstone project.',
  },
  {
    title: 'Hardware Requirements',
    link: '/docs/hardware-requirements',
    description: 'Review the recommended and minimum hardware specifications for your workstation and edge kits.',
  },
  {
    title: 'Robot Lab Options',
    link: '/docs/robot-lab',
    description: 'Explore various options for accessing physical robot hardware and lab facilities.',
  },
  {
    title: 'Cloud Lab Options',
    link: '/docs/cloud-lab',
    description: 'Discover how cloud computing resources can accelerate your robotics development.',
  },
  {
    title: 'Student Kits',
    link: '/docs/student-kits',
    description: 'Learn about recommended student kits for hands-on experimentation with physical robotics.',
  },
];

function Feature({title, description, link}: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className="card padding--lg text--center">
        <h3>{title}</h3>
        <p>{description}</p>
        <div className="margin-top--md">
          <Link
            className="button button--primary"
            to={link}>
            Read Chapter
          </Link>
        </div>
      </div>
    </div>
  );
}

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <h1 className="hero__title">{"Physical AI & Humanoid Robotics"}</h1>
        <p className="hero__subtitle">{"Exploring embodied intelligence, robot perception, and autonomous systems for a new era of human-robot collaboration."}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/course-details">
            Start Learning
          </Link>
        </div>
      </div>
    </header>
  );
}

function HomepageFeatures(): JSX.Element {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}

export default function Home(): JSX.Element {
  return (
    <Layout
      title={`Hello from ${useDocusaurusContext().siteConfig.title}`}
      description="Description will go into a meta tag in <head />">
      <HomepageHeader />
      <main>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}

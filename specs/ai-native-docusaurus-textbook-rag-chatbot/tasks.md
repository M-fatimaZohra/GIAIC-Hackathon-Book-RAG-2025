# AI-Native Docusaurus Textbook + RAG Chatbot Tasks

## Step 0: Install Required Tools & Frameworks
# Claude should ensure the following are installed:
# - Node.js (LTS) & npm (for Docusaurus)
# - Docusaurus (npx create-docusaurus)
# - Git (for version control & GitHub push)
# - Python 3.10+ (for FastAPI backend & ROS2 Python nodes)
# - FastAPI (pip install fastapi uvicorn)
# - Qdrant client (pip install qdrant-client)
# - OpenAI Agents / ChatKit SDKs
# - Spec-Kit Plus (already installed)
# - Claude Code (already installed)
# - Better-Auth (optional, for signup/signin)

## Step 1: Generate Book Content in Docusaurus
- Input: Course content for Physical AI & Humanoid Robotics (modules 1–4, capstone, hardware, labs)
- Generate chapters:
  - Preface: course goal, focus, learning outcomes
  - Module 1: The Robotic Nervous System (ROS 2)
      - Topics: ROS 2 nodes, topics, services, Python bridging (rclpy), URDF
      - Exercises, code snippets, diagrams
  - Module 2: The Digital Twin (Gazebo & Unity)
      - Topics: physics simulation, gravity, collisions, LiDAR, depth cameras, IMUs, Unity visualization
      - Exercises, diagrams, examples
  - Module 3: The AI-Robot Brain (NVIDIA Isaac)
      - Topics: Isaac Sim, Isaac ROS, VSLAM, Nav2 path planning
      - Exercises, code snippets, diagrams
  - Module 4: Vision-Language-Action (VLA)
      - Topics: OpenAI Whisper voice commands, LLM cognitive planning, robot action sequences
      - Exercises, diagrams
  - Module 5: Capstone Project: Autonomous Humanoid
      - Complete step-by-step project using simulated robot
      - Include diagrams, obstacles, voice command examples
  - Appendices: Sensors primer, robotics math, glossary, hardware setup guides
  - Bonus/Optional: placeholders for personalization, Urdu translation, RAG integration
- Ensure all exceptions and errors are handled professionally
- Ask clarifying questions if content is ambiguous

## Step 2: Build Docusaurus Project
- Folder name: physical-ai-and-humanoid-robotics/
- Generate sidebar, MDX files, docs structure
- Include custom components if needed
- Retry or log errors if build fails

## Step 3: Push to GitHub
- Claude Code deploys automatically to a public GitHub repo
- Store repo URL in project metadata

## Step 4: Deploy to GitHub Pages
- Publish book automatically
- Store published URL for RAG integration

## Step 5: Build RAG Chatbot
- Claude Code subagents:
  - Extract content from Docusaurus book
  - Index with Qdrant Cloud Free Tier
  - Integrate with FastAPI backend using OpenAI Agents / ChatKit SDK
- Ensure accurate answers, cite chapter/section, handle errors, avoid hallucinations

## Step 6: Optional Features (Bonus Points)
- Signup / Signin using Better-Auth; collect user software/hardware background
- Personalization: adapt chapter content dynamically based on user profile.
- Urdu Translation: translate chapters using Claude Code subagent
- Reusable intelligence: create subagents for content, diagrams, code, and RAG interactions

## Step 7: Testing & Validation
- Validate book links, frontend load, RAG chatbot responses, optional features
- Log errors; retry failed steps automatically
- Ensure all outputs are free of hallucinations, broken links, or crashes.

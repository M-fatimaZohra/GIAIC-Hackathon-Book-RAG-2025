# Content Creation Skill

## YAML Frontmatter
```yaml
name: content-creation-skill
description: A sub-skill for expanding short topic summaries into full documentation topics suitable for Docusaurus MDX files
version: 1.0.0
```

## When to Use This Skill

Use this skill when you need to:
- Expand a brief topic summary into a comprehensive documentation page
- Generate structured, educational content for Docusaurus sites
- Create MDX-compatible content that follows documentation conventions
- Transform minimal input data into detailed, well-formatted explanations
- Ensure content is progressive from beginner to advanced levels

## Process Steps

1. **Receive Input Parameters**
   - Extract topic name
   - Extract topic summary
   - Identify optional references or context links
   - Determine target reading level (beginner to advanced)

2. **Analyze and Structure Content**
   - Parse the topic summary for core concepts
   - Plan content structure with logical flow
   - Determine appropriate sections and subsections
   - Identify potential examples or use cases

3. **Enhance Content with Research**
   - Consult web resources for accurate information
   - Reference existing documentation in the same book if available
   - Gather best practices and common patterns
   - Verify technical accuracy of concepts

4. **Generate MDX Content**
   - Create YAML frontmatter with title and sidebar_label
   - Write introductory section based on topic summary
   - Develop core concepts with definitions and explanations
   - Add practical examples and use cases
   - Include best practices and common pitfalls
   - Conclude with summary section

5. **Apply Formatting Standards**
   - Use proper MDX headings hierarchy (#, ##, ###)
   - Apply correct indentation and spacing
   - Ensure code blocks are properly formatted
   - Validate MDX syntax compatibility
   - Maintain consistent style throughout

6. **Validate Output Quality**
   - Check for logical flow and readability
   - Verify content progresses from beginner to advanced
   - Ensure no invalid MDX symbols or formatting errors
   - Confirm content stays within provided topic scope

## Output Format

The skill will output:
1. Complete MDX content ready for insertion into Docusaurus
2. Proper YAML frontmatter with title and sidebar_label
3. Structured content with appropriate headings hierarchy
4. Beginner-friendly to advanced level progression
5. Validated MDX syntax with no formatting errors

## Example

### Input
```
Topic name: "Modal Dialogs"
Topic summary: "Learn how to implement accessible modal dialogs in React."
Target reading level: "beginner to advanced"
```

### Output
```
---
title: Modal Dialogs
sidebar_label: Modal Dialogs
---

# Modal Dialogs

Modal dialogs are interactive pop-up interfaces that temporarily capture user attention. They're commonly used for alerts, confirmations, or collecting user input without navigating away from the current page.

## Introduction to Modals

Modals, also known as dialog boxes, overlay the main content and require user interaction before returning to the main application. They should be used sparingly to avoid disrupting the user experience.

## Basic Implementation

In React, you can implement a basic modal using conditional rendering:

```jsx
import React, { useState } from 'react';

const Modal = ({ isOpen, onClose, children }) => {
  if (!isOpen) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <button onClick={onClose}>Close</button>
        {children}
      </div>
    </div>
  );
};
```

## Accessibility Considerations

Properly implemented modals must be accessible to all users, including those using screen readers:

- Trap focus within the modal
- Restore focus to the trigger element when closing
- Use appropriate ARIA attributes
- Provide keyboard navigation

## Advanced Patterns

For more complex applications, consider using libraries like React Aria or Reach UI that provide pre-built, accessible modal components with features like:

- Proper focus management
- Keyboard navigation
- Screen reader announcements
- Overlay scrolling prevention

## Best Practices

- Use modals sparingly and only for important interactions
- Keep modal content concise
- Always provide a clear way to close the modal
- Consider mobile responsiveness
- Test with keyboard navigation and screen readers

## Summary

Modal dialogs are powerful UI elements that require careful implementation to ensure accessibility and usability. Following established patterns and testing thoroughly will result in a better user experience.
```
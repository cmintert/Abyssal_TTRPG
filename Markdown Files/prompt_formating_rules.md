
Prompt Formatting Rule for General Component Template
Objective:
Ensure that prompts are clearly structured, easy to read, and consistently formatted when writing or editing in a Markdown-friendly environment, like PyCharm or any text editor. This guide outlines the structure, formatting, and stylistic choices that should be applied to maintain consistency across all prompt templates.

1. Prompt Title and Headers
Title: Begin the prompt with a clear, descriptive title using an H2 header (##).
Subsections: Use H3 headers (###) to break down the prompt into logical sections. Each section should have a clear and concise header.
Example:

markdown
Copy code
## General Component Template Prompt
2. Prompt Sections
Start of Prompt: Clearly denote the beginning of the prompt text using an "### Start of Prompt ###" marker.
End of Prompt: Use "### End of Prompt ###" at the end of the prompt text to clearly indicate the end.
Example:

markdown
Copy code
### Start of Prompt ###
...
### End of Prompt ###
3. Instructions and Context
Provide clear instructions on what the prompt should achieve. Use inline code formatting for any variables or placeholders ([Placeholder]).
If specific values or attributes need to be described, list them in bullet points under appropriate headers.
Example:

markdown
Copy code
Please design a new component for `[Component Type]` in a space vessel. The component should `[describe the function and special features]`.
4. Lists and Formatting
Bulleted Lists: Use bullet points (-) to list attributes, options, or instructions.
Indentation: Maintain consistent indentation for sub-bullets and nested lists.
Bold Text: Highlight important terms or section titles with bold text (**Bold**).
Example:

markdown
Copy code
- **Small Components (1 Slot):**
  - Basic Sensors
  - Small Utility Systems
5. Types and Value Ranges
When specifying types or value ranges, clearly indicate the type in brackets next to the attribute name.
List possible values in parentheses or as part of the description.
Example:

markdown
Copy code
#### Component Size [type: integer]:
- **Small Components (1 Slot):**
  - Basic Sensors
6. Code Blocks for Examples
Use fenced code blocks with the appropriate language identifier (e.g., ```python) for any code examples or structures you want to highlight.
Ensure code blocks are properly indented and formatted to match Python syntax.
Example:

markdown
Copy code
```python
{
    "data": {
        "Component Name": "Example Component",
        "Type": "Component Type",
        "Component Size": "Small",
        ...
    },
    "type": "component"
},
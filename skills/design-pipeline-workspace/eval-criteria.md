# Evaluation Criteria for Design Pipeline Skill

## What we're looking for across all test cases

### 1. Mode Recognition
- Did the skill ask about running mode (guided vs automated)?
- Did it correctly interpret the user's preference from context?

### 2. Research Routing
- Did it correctly identify whether research exists or needs to be created?
- Did it route to the right research type (market vs user)?
- Did it skip re-running research when the user provided findings?

### 3. Stage Sequencing
- Did stages run in the correct order?
- Did each stage receive context from prior stages (especially the research report)?

### 4. Checkpoint Behavior
- Guided: Did it pause at each stage for user confirmation?
- Automated: Did it run straight through without pausing?

### 5. Design System Usage
- Did outputs use Software DS / Design System Lab components?
- Did it reference tokens from colors.css?

### 6. Self-Challenge (Product Design)
- Did the product design stage challenge its own concepts against the research?
- Did it document reasoning for its design decisions?

### 7. Multi-Pass Evaluation
- Did critique/heuristics run 3 passes?
- Did accessibility run 3 passes?
- Were findings from each pass documented?

### 8. Output Completeness
- Research report HTML
- Journey map HTML
- IA flows
- Design concepts
- Critique/heuristic findings
- Accessibility findings
- Research evaluation
- Component gap report

### 9. Comparison: With-Skill vs Without-Skill
- Is the with-skill output more structured and complete?
- Does the skill version follow a more disciplined pipeline?
- Does the baseline miss stages or skip evaluation loops?

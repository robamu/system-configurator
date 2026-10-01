## Tools

- Prefer `rg` over `grep` for grepping

## Rules for writing code documentation

- You tend to write very verbose documentation, almost to the point of docs becoming noise.
- Good names, good structures should be preferred to extensive documentation
- If something is self-explanatory, there is no need to add additional documentation, unless
  there is a rule like required documentation of public fields.
- The most important documentation is everything that is not obvious from the code: Special rules,
  reasons on why the code is the way it is (if it is not obvious from the context), trade-offs..
- Try to avoid ; and --. I have never seen that kind of punctuation seen much in technical
  documentation
- Sometimes, you documentation tend to gravitate towards rambling. Keep the sentences simple and
  understandable. There is beauty in simplicity.

## Rules for writing commit message

- You tend to write very verbose commit messages, almost to the point of docs becoming noise.
- Sometimes, your commit messages tend to gravitate towards rambling. Keep the sentences simple and
  understandable. There is beauty in simplicity.
- Prefer bullet lists over flowing prose paragraphs when describing multiple changes.
- Never create commits yourself. Stage the changes and stop. I write every commit message
  myself, so I understand each change.
- Never use a `Co-Authored-By` trailer. When I ask for a trailer, use
  `Assisted-by: Claude <model> <noreply@anthropic.com>` with the model name, for example
  `Assisted-by: Claude Opus 5.5 <noreply@anthropic.com>`.
- You can point out problems in my commit messages, but do not rewrite them unless I ask.

## Scope discipline

- Never bundle unrelated changes into one branch or commit (e.g. an i2c fix and an spi.rs cleanup).
  One logical change per branch/commit.
- Before large multi-file refactors or speculative additions, state the plan in 2-3 bullets and
  wait for confirmation.


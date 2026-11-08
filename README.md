# CBSE Mathematics 2015 — Combined Engineering-Methods Edition

This branch introduces a single combined LaTeX source for the Class 10 and Class 12
2015 papers. The root-level \`main.tex\` is the combined build entry point.

## Document structure

1. **Class 10 Mathematics 2015**
   - Formulae
   - Problems
2. **Class 12 Mathematics 2015**
   - Formulae
   - Problems

Original paper question numbers are preserved, including gaps where a question is
not part of the production edition. Section, subsection, question, formula, and
equation indices are generated from LaTeX counters; the source no longer prints
question numbers as manual item labels.

## Build

Install a TeX Live distribution with IEEEtran, \`tfrupee\`, \`tkz-euclide\`,
\`circuitikz\`, and the packages imported by the reference style files. Then run:

\`\`\`bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
\`\`\`

The source figures remain in their class-specific \`figs/\` directories. The
combined document sets \`\\graphicspath\` to both class directories.

The GitHub Actions workflow in \`.github/workflows/build-combined-pdf.yml\`
rebuilds the PDF and runs focused numerical checks for C10-Q22, C12-Q24, and
C12-Q48. It publishes the generated PDF as a workflow artifact and commits the
build output to the working branch only after a successful build.

## Production exclusions

See [audit/PRODUCTION_DECISIONS.md](audit/PRODUCTION_DECISIONS.md). C10-Q23 and
C12-Q58 are excluded by the approved production decisions. C12-Q20, Q21, and
Q22 are also excluded because their actual statements do not meet the later
Laplace-transform-primary requirement. Their original method assignments are
retained only in the audit record.

## Engineering-method migration status

See [audit/ADVANCED_METHOD_MAP.csv](audit/ADVANCED_METHOD_MAP.csv). Rows marked
\`UPDATED\` have been migrated and checked in this branch; rows marked
\`PENDING_REWRITE\` are not yet cleared for a final release. Do not treat this
working branch as a completed final edition until every in-scope row is
resolved and verified.

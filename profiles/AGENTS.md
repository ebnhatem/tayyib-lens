# profiles/ — fiqh line definitions

## Rules
- One profile per file: id, line, description, mode, inheritance.
- All profiles inherit universal-prohibitions.
- A new profile requires: a coherent published line, its own evidence set in
  knowledge/, and maintainer approval via issue/PR BEFORE the files land.
- Never editorialize inside a profile — the description states the line's published
  position and its institutional sources, nothing more.

## Committing
`feat(profiles): add <profile-name> (<line>)` — with the source set in the body.

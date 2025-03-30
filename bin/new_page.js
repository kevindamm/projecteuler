#!/usr/bin/env node

/**
 * @file new_page.js
 * @example npm x begin 42
 * 
 * Simple Node.js script for generating the boilerplate of a new blog post.
 * 
 * @param integer (required) the problem number (according to ProjectEuler.net)
 */

import path from 'node:path';
import { existsSync } from 'node:fs';
import { Buffer } from 'node:buffer';
import { readFile, writeFile } from 'node:fs/promises';

import fetch from 'node-fetch';

const { log, error } = console;


const today = new Date();
const problem_number = argvProblemNumber();
const digits_padded = String(problem_number).padStart(4, '0');
const filepath = path.join('.', 'pages',
  digits_padded.concat('.md'));
if (existsSync(filepath)) {
  error(`File ${filepath} already exists, ` +
    `delete it first if you intended to overwrite it.`);
  process.exit(1);
}
log(`Generating new article page for ${filepath} ...`);


const { titles } = JSON.parse(await readFile("./public/pe100.json", "utf-8"))
const title = title_if_known(titles, problem_number)
const problem_description = await fetchDescription(problem_number);

// If you aren't me, feel free to change the author name and other frontmatter.
// If you're using this for your own writeup, feel free to change the structure.
const template = `---
title: ${title}
author: Kevin Damm
date: ${today.toISOString().substring(0, 10)}
---

# PE ${digits_padded}: {{ $frontmatter.title }}

<pe100-problem n="${problem_number}">

${problem_description}

</pe100-problem>

---

[toc]


This is just a stub until the article is written.
`;


try {
  await writeFile(
    filepath,
    new Uint8Array(Buffer.from(template)));
} catch (err) {
  error(err);
}

log(`Done writing template for problem ${problem_number}.`);
process.exit(0);


// Parses the problem number from the first command-line argument.
function argvProblemNumber() {
  if (!process.argv[2]) {
    error('must call with at least one argument (the problem number)');
    process.exit(1);
  }
  const problem_number = Number(process.argv[2]);
  if (!problem_number) {
    error('failed to parse the problem ID (it must be a number)');
    process.exit(1);
  }
  return problem_number
}

// retrieves the title for any problem between #1 to #100.
function title_if_known(titles, pe_num) {
  if (!pe_num ||
    typeof(pe_num) != "number" ||
    pe_num < 1 || pe_num >= titles.length) {
    return titles[0] || "<<UNK>>";
  }
  return titles[pe_num];
}

// Fetches from projecteuler.net the LaTeX-formatted problem description.
async function fetchDescription(problem_number) {
  const url = 'https://projecteuler.net/minimal='.concat(problem_number);
  log(`Fetching problem description from ${url} ...`);
  const description = await fetch(url).then((response) => response.text());
  return description
    .replaceAll('</p>', '')
    .replaceAll('<p>', '\n')
    .trim();
}

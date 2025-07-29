#!/usr/bin/env node

/**
 * @file new_golang.js
 * @example npm x new-golang 42
 * 
 * Generates the boilerplate of a new Go solution.
 * 
 * @param integer (required) the problem number (according to ProjectEuler.net)
 */

import path from 'node:path';
import { existsSync } from 'node:fs';
import { Buffer } from 'node:buffer';
import { readFile, writeFile } from 'node:fs/promises';

if (!process.argv[2]) {
  console.error('must call with a numeric argument (the problem ID)');
  process.exit(1);
}
const problem_number = Number(process.argv[2]);
if (!problem_number) {
  console.error('failed to parse the problem ID from the first argument (it must be a number)');
  process.exit(1);
}

const digits_padded = String(problem_number).padStart(4, '0');
const filepath = path.join('.', 'golang',
  'p'.concat(digits_padded).concat('.go'));
if (existsSync(filepath)) {
  error(`File ${filepath} already exists, ` +
    `delete it first if you intended to overwrite it.`);
  process.exit(1);
}

const titles = await readTitles();
const problem_title = titleIfKnown(titles, problem_number);
const title_fn = fnNameFromTitle(titles, problem_number);

// If you aren't me, feel free to change the author name.
const template = `// Copyright (c) 2025 Kevin Damm
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
//
// github:kevindamm/projecteuler/golang/p${digits_padded}.go

package solutions

/*
 * Problem ${problem_number} - ${problem_title}
 */

func ${title_fn}(limit int) int64 {
  value := int64(0)

  return value
}
`;


try {
  await writeFile(
    filepath,
    new Uint8Array(Buffer.from(template)));
} catch (err) {
  console.error(err);
}

console.log(`Done writing Go boilerplate to ${filepath}.`);
process.exit(0);


function titleIfKnown(titles, pe_num) {
  if (!pe_num ||
    typeof(pe_num) != "number" ||
    pe_num < 1 || pe_num >= titles.length) {
    return titles[0];
  }
  const title = titles[pe_num];

  if (!title || title === titles[0]) {
    return "SolutionFunction";
  }
  return title.replaceAll(/ (\w)/g,
      (match) => match.slice(1).toUpperCase());
}

function fnNameFromTitle(title) {
  if (!title || title === titles[0]) {
    return "SolutionFunction";
  }
  return title.
    replaceAll(/[_\t,'"-]/g, "").
    replaceAll(/[\s-]([\w\d])/g, (match) => match.slice(1).toUpperCase());
}

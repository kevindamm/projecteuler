#!/usr/bin/env node

/**
 * @file new_python.js
 * @example npm x new-python 42
 * 
 * Generates the boilerplate of a new Python solution.
 * 
 * @param integer (required) the problem number (according to ProjectEuler.net)
 */

import path from 'node:path';
import { existsSync } from 'node:fs';
import { Buffer } from 'node:buffer';
import { readFileSync, writeFileSync, appendFileSync } from 'node:fs';

if (!process.argv[2]) {
  console.error('must call with a numeric argument (the problem ID)');
  process.exit(1);
}
const problem_number = Number(process.argv[2]);
if (!problem_number) {
  console.error('failed to parse the problem ID from the first argument (it must be a number)');
  process.exit(1);
}

const project_rootdir = process.env.INIT_CWD;
const digits_padded = String(problem_number).padStart(4, '0');
const filepath = path.join(project_rootdir, 'python');

if (!existsSync(filepath)) {
  console.error(`File directory ${filepath} not found.
   Make sure process.env is initialized (are you running with npm x?)`);
  process.exit(1);
}

const src_filepath = path.join(filepath,
  'p'.concat(digits_padded).concat('.py'));

if (existsSync(src_filepath)) {
  console.error(`File ${filepath} already exists, ` +
    `delete it first if you intended to overwrite it.`);
  process.exit(1);
}
const test_filepath = path.join(filepath, "test_solve.py")

const titles = await readTitles();
const problem_title = titleIfKnown(problem_number);
const title_fn = fnNameFromTitle(problem_title);

// If you aren't me, feel free to change the author name.
const src_boilerplate = `# Copyright (c) 2025 Kevin Damm
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# github:kevindamm/projecteuler/python/p${digits_padded}.py

"""Problem ${problem_number} - ${problem_title}"""

def ${title_fn}(value: int) -> int:
  pass


if __name__ == "__main__":
  print(${title_fn}())
`;


const module = `p${digits_padded}`;
const test_boilerplate = `
  def test_${module}(self):
    import ${module}
    self.assertEqual(
      ${module}.${title_fn}(),
      )#answer
`;


try {
  await writeFileSync(
    src_filepath,
    new Uint8Array(Buffer.from(src_boilerplate)));
  console.log(`Successfully wrote Python boilerplate to ${src_filepath}.`);

  await appendFileSync(
    test_filepath,
    new Uint8Array(Buffer.from(test_boilerplate)));
  console.log(`Successfully wrote Python boilerplate to ${test_filepath}.`);
} catch (err) {
  console.error(err);
}


process.exit(0);


async function readTitles() {
  const metadata = JSON.parse(readFileSync("public/pe100.json", "utf8"));
  return metadata?.titles;
}

function titleIfKnown(pe_num) {
  if (!pe_num ||
    typeof(pe_num) != "number" ||
    pe_num < 1 || pe_num >= titles.length) {
    return titles[0];
  }
  return titles[pe_num];
}

function fnNameFromTitle(title) {
  if (!title || title === titles[0]) {
    return "SolutionFunction";
  }
  return title.
    replaceAll(/[_\t,-]/g, "").
    replaceAll(/[\s-]([\w\d])/g, (match) => match.slice(1).toUpperCase());
}

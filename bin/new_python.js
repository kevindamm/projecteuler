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
import { writeFile } from 'node:fs/promises';

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
const filepath = path.join('.', 'python',
  'p'.concat(digits_padded).concat('.py'));
if (existsSync(filepath)) {
  error(`File ${filepath} already exists, ` +
    `delete it first if you intended to overwrite it.`);
  process.exit(1);
}

// If you aren't me, feel free to change the author name.
const template = `# Copyright (c) 2025 Kevin Damm
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


if __name__ == "__main__":
  pass
`;


try {
  await writeFile(
    filepath,
    new Uint8Array(Buffer.from(template)));
} catch (err) {
  console.error(err);
}

console.log(`Done writing Python boilerplate to ${filepath}.`);
process.exit(0);

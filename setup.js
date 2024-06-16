import { execSync } from "child_process";
import path from "path";
import { fileURLToPath } from "url";
import fs from "fs/promises";
import pool from "./app/db/db.js";
import { readJsonFile } from "./app/utils/readJsonFile.js";



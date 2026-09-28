// Optional local preview. Only Node built-ins are used; no npm install needed.
import { createServer } from 'node:http';
import { createReadStream } from 'node:fs';
import { stat } from 'node:fs/promises';
import { extname, resolve, sep } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('../', import.meta.url));
const args = process.argv.slice(2);
const portArg = args.indexOf('--port');
const hostArg = args.indexOf('--host');
const port = Number(portArg >= 0 ? args[portArg + 1] : process.env.PORT || 4173);
const host = hostArg >= 0 ? args[hostArg + 1] : process.env.HOST || '0.0.0.0';
const mime = { '.html': 'text/html; charset=utf-8', '.css': 'text/css; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.json': 'application/json; charset=utf-8', '.webp': 'image/webp', '.png': 'image/png', '.jpg': 'image/jpeg', '.svg': 'image/svg+xml', '.mp4': 'video/mp4', '.pdf': 'application/pdf' };
const server = createServer(async (req, res) => {
  try {
    let pathname = decodeURIComponent(new URL(req.url, 'http://localhost').pathname);
    if (pathname.endsWith('/')) pathname += 'index.html';
    const path = resolve(root, '.' + pathname);
    if (!path.startsWith(root.endsWith(sep) ? root : root + sep)) {
      res.writeHead(403); res.end('Forbidden'); return;
    }
    const info = await stat(path);
    if (!info.isFile()) throw new Error('Not a file');
    const headers = { 'Content-Type': mime[extname(path)] || 'application/octet-stream', 'Accept-Ranges': 'bytes', 'Cache-Control': 'no-cache' };
    const match = /^bytes=(\d+)-(\d*)$/.exec(req.headers.range || '');
    if (match) {
      const start = Number(match[1]);
      const end = match[2] ? Math.min(Number(match[2]), info.size - 1) : info.size - 1;
      if (start > end || start >= info.size) { res.writeHead(416, { 'Content-Range': `bytes */${info.size}` }); res.end(); return; }
      res.writeHead(206, { ...headers, 'Content-Length': end - start + 1, 'Content-Range': `bytes ${start}-${end}/${info.size}` });
      if (req.method === 'HEAD') res.end(); else createReadStream(path, {start, end}).pipe(res);
    } else {
      res.writeHead(200, { ...headers, 'Content-Length': info.size });
      if (req.method === 'HEAD') res.end(); else createReadStream(path).pipe(res);
    }
  } catch {
    res.writeHead(404, {'Content-Type': 'text/plain; charset=utf-8'}); res.end('Page not found');
  }
});
server.listen(port, host, () => console.log(`Portfolio preview listening on ${host}:${port}`));

console.log('Welcome to Holberton School, what is your name?');

// キーの入力待ち状態にする。
process.stdin.resume();
process.stdin.setEncoding('utf8');

// 標準入力終了時のイベント処理
process.stdin.on('end', () => {
  console.log('This important software is now closing');
});

// Ctrl + C が入力された場合のイベント処理
process.on('SIGINT', () => {
  console.log('This important software is now closing');
  // SIGINTイベントでは、プログラムを明示的に終了させるためにprocess.exit(0)を呼び出す
  process.exit(0);
});

process.stdin.on('readable', () => {
  const input = process.stdin.read();
  if (input !== null) {
    process.stdout.write(`Your name is: ${input}`);
  }
});

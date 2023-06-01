function debounce(fn, t) {
  let timeout;
  
  return function debouncedFunction(...args) {
    clearTimeout(timeout); // Clear the previous timeout
  
    timeout = setTimeout(() => {
      fn.apply(this, args); // Execute the provided function after the delay
    }, t);
  }
}

// Example usage
const start = Date.now();

function log() {
  console.log(Date.now() - start);
}

const debouncedLog = debounce(log, 20);

setTimeout(debouncedLog, 10); // cancelled
setTimeout(debouncedLog, 20); // logs: 40
setTimeout(debouncedLog, 50); // cancelled
setTimeout(debouncedLog, 60); // logs: 80
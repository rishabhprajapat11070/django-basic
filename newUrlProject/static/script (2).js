// Types out a fake JSON API response inside the home page terminal.
// No-ops harmlessly on pages that don't have #jsonOut.
(function () {
  const el = document.getElementById("jsonOut");
  if (!el) return;

  const lines = [
    { text: "{", cls: "" },
    { text: '  "name": "Your Name",', cls: "" },
    { text: '  "role": "Python Backend Developer",', cls: "" },
    { text: '  "focus": ["FastAPI", "SQLAlchemy", "REST APIs"],', cls: "" },
    { text: '  "available_for_hire": true,', cls: "" },
    { text: '  "response_time": "< 24h"', cls: "" },
    { text: "}", cls: "" }
  ];

  function colorize(line) {
    return line
      .replace(/"([a-zA-Z_]+)":/g, '<span class="k">"$1"</span>:')
      .replace(/: "([^"]*)"/g, ': <span class="s">"$1"</span>')
      .replace(/: (true|false)/g, ': <span class="b">$1</span>');
  }

  const prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (prefersReduced) {
    el.innerHTML = lines.map(l => colorize(l.text)).join("\n");
    return;
  }

  let out = "";
  let li = 0, ci = 0;

  function typeChar() {
    if (li >= lines.length) {
      el.innerHTML = lines.map(l => colorize(l.text)).join("\n");
      return;
    }
    const line = lines[li].text;
    if (ci <= line.length) {
      const doneLines = lines.slice(0, li).map(l => colorize(l.text)).join("\n");
      const currentPartial = line.slice(0, ci);
      out = (doneLines ? doneLines + "\n" : "") + colorize(currentPartial) + '<span class="caret"></span>';
      el.innerHTML = out;
      ci++;
      setTimeout(typeChar, 14 + Math.random() * 18);
    } else {
      li++;
      ci = 0;
      setTimeout(typeChar, 90);
    }
  }

  setTimeout(typeChar, 350);
})();

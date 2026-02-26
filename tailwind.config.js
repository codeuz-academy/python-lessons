/** @type {import('tailwindcss').Config} */
function stripMarkdownCodeBlocks(content) {
  if (typeof content !== "string") {
    return content;
  }

  // Avoid generating utilities from markdown code examples.
  return content.replace(/```[\s\S]*?```/g, "");
}

module.exports = {
  content: {
    files: [
      "./_includes/**/*.njk",
      "./_layouts/**/*.njk",
      "./tools/**/*.njk",
      "./tutorial/**/*.md",
      "./uz/**/*.md",
      "./*.{md,njk}",
    ],
    transform: {
      md: stripMarkdownCodeBlocks
    }
  },
  theme: {
    extend: {
      colors: {
        primary: {
          100: '#e0f2fe',
          200: '#bae6fd',
          300: '#3776ab',
          400: '#316997',
          500: '#2a5880',
          600: '#234c6e',
          700: '#1d3f5b',
          800: '#1c3a55',
          900: '#1e2933'
        },
        secondary: {
          400: '#ffdf76',
          500: '#fdd03f',
          700: '#e2b215',
        }
      },
      animation: {
        scroll: 'scroll 80s linear infinite',
      },
      keyframes: {
        scroll: {
          '0%': { transform: 'translateX(0)' },
          '100%': { transform: 'translateX(-50%)' },
        },
      },
    },
  },
  plugins: [],
}

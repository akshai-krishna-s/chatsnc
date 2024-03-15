/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        'blue-primary': '#128FEA',
        'gray-dark': '#1D1F28',
        gray: '#737373',
        'gray-medium': '#282A36',
        'gray-light': '#DEDEDE',
        shadow: 'rgba(82, 88, 123, 0.32)',
      },
      fontFamily: {
        roboto: ['Roboto', 'sans-serif'],
        open: ['Open Sans', 'sans-serif'],
      },
    },
  },
  plugins: [],
}

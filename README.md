<div align="center">
  <h1>🌌 Antigravity Workflow Lab</h1>
  <p><em>Premium Dark Mac OS Window & Animated SVG Node Workflows</em></p>
  
  [![React](https://img.shields.io/badge/React-19.0-blue?style=for-the-badge&logo=react)](https://reactjs.org/)
  [![Vite](https://img.shields.io/badge/Vite-8.0-646CFF?style=for-the-badge&logo=vite)](https://vitejs.dev/)
  [![Framer Motion](https://img.shields.io/badge/Framer_Motion-12.0-black?style=for-the-badge&logo=framer)](https://framer.com/motion)
  [![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-v4.0-06B6D4?style=for-the-badge&logo=tailwind-css)](https://tailwindcss.com/)
</div>

<br/>

> **Demo Suggestion:** *Upload a `.gif` or `.webp` of your workflow running here! Replace this block with `![Workflow Demo](./preview.gif)`*

## ✨ Interactive Features

Each node in the ecosystem behaves autonomously and triggers a specific data flow through the canvas. The lines are rendered via responsive `<svg>` curves (`stroke-dashoffset` animation) and glow using custom SVG filters.

| Node | Glow Color | Effect Triggered on Hover |
| :--- | :--- | :--- |
| **Trigger** | ![#00E5FF](https://placehold.co/15x15/00E5FF/00E5FF.png) `#00E5FF` | Master node. Emits a cyan neon glow across main connection paths. |
| **LLM** | ![#A855F7](https://placehold.co/15x15/A855F7/A855F7.png) `#A855F7` | Branches out purple neon flows towards the Notion database and Status Badge. |
| **Email** | ![#F59E0B](https://placehold.co/15x15/F59E0B/F59E0B.png) `#F59E0B` | Activates the orange flow sequence leading towards the LLM node. |
| **Slack** | ![#3B82F6](https://placehold.co/15x15/3B82F6/3B82F6.png) `#3B82F6` | Node emits a continuous blue light pulse. Connects down to the Status Badge. |
| **Notion** | ![#EC4899](https://placehold.co/15x15/EC4899/EC4899.png) `#EC4899` | Triggers a pink data flow path straight to the Status Badge node. |

> **Fluid Levitation:** All nodes share a strict 4-second `Framer Motion` levitation with staggered delays to achieve a natural, floating ecosystem feel over the `#0B0E14` technical grid background.

---

## ⚙️ System Configuration

To run this laboratory correctly on a Windows environment using PowerShell, we applied specific configurations:

### 1. PowerShell Execution Policy
By default, Windows may block Vite and other Node module execution scripts. You must enable `RemoteSigned` policies on your machine to permit local script execution:
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 2. Node.js & Vite Setup
Dependencies were installed locally, bypassing global installations by using `npx`. Run the following to replicate the environment:
```bash
# 1. Install local dependencies
npm install react-dom vite @vitejs/plugin-react tailwindcss @tailwindcss/vite typescript @types/react @types/react-dom

# 2. Spin up the Vite Dev Server
npx vite --port 3000
```

---

## 📝 Commit History Guide

To maintain a clean and professional repository history, please follow this commit sequence when pushing to GitHub:

1. **`feat: initialize project structure with vite and tailwind v4`**
   *Configured the dev environment, installed React, Framer Motion, and setup the Vite config.*
2. **`feat: implement mac os window frame and dark premium grid`**
   *Added the base structural UI container, header dots, and the #0B0E14 custom background.*
3. **`feat: create base floating node component with framer motion`**
   *Implemented staggered 4s levitation mechanics and glassmorphism styling for nodes.*
4. **`feat: setup responsive svg canvas and bezier connection paths`**
   *Added the SVG layer using `foreignObject` integration for pixel-perfect resizing without misalignment.*
5. **`feat: implement global anti-jump dash animation`**
   *Injected CSS `@keyframes` and `stroke-dashoffset` magic numbers for a continuous optical illusion flow.*
6. **`feat: add universal distinct neon hover states`**
   *Integrated specific node branding colors (Cyan, Purple, Orange, Blue, Pink) for isolated flow triggers and pulse animations.*
7. **`docs: finalize interactive documentation and system configurations`**
   *Wrote the comprehensive README including PowerShell setup and feature showcase.*

<br/>

<div align="center">
  <p>Crafted for the <a href="https://thekaix.com">thekaix.com</a> Lab.</p>
</div>

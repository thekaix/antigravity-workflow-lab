import React from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import WorkflowAnimation from './components/ui/branding/WorkflowAnimation'

const root = createRoot(document.getElementById('root')!)
root.render(<WorkflowAnimation />)

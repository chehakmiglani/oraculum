const BASE = import.meta.env.VITE_API_BASE_URL || '' // when empty, use Vite proxy

async function http<T>(path: string, options: RequestInit = {}, timeoutMs = 20000): Promise<T> {
  const controller = new AbortController()
  const id = setTimeout(() => controller.abort(), timeoutMs)
  try {
    const res = await fetch(`${BASE}${path}`.replace(/\/+/g, '/'), { ...options, signal: controller.signal })
    if (!res.ok) {
      const text = await res.text().catch(() => '')
      throw new Error(`HTTP ${res.status} ${res.statusText} ${text}`)
    }
    return (await res.json()) as T
  } finally {
    clearTimeout(id)
  }
}

export function getHistory() {
  return http<{ items: Array<{ tool: string; summary: string }> }>('/api/history')
}

export function askChat(question: string) {
  return http<{ answer: string; provider: string; model: string }>(
    '/api/chat',
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question }),
    },
  )
}

export function analyzeResume(file: File) {
  const fd = new FormData()
  fd.append('file', file)
  return http<{ filename: string; feedback: string }>(
    '/api/resume/analyze',
    { method: 'POST', body: fd },
    60000,
  )
}

export function generateRoadmap(target_role: string, experience_level: string) {
  return http<{ steps: string[] }>(
    '/api/roadmap',
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ target_role, experience_level }),
    },
  )
}

export function generateCoverLetter(job_description: string, resume_text?: string) {
  return http<{ letter: string }>(
    '/api/cover-letter',
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ job_description, resume_text }),
    },
  )
}
import { useState, useEffect } from 'react'
import type { Manifest } from '../types'

export function useManifest() {
  const [manifest, setManifest] = useState<Manifest | null>(null)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetch('/manifests/manifest_001.json')
      .then(r => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`)
        return r.json()
      })
      .then(setManifest)
      .catch(e => setError(e.message))
  }, [])

  return { manifest, error }
}

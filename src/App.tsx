import { useState } from 'react'
import { useManifest } from './hooks/useManifest'
import { MapViewer } from './components/MapViewer'
import { ChunkPanel } from './components/ChunkPanel'
import type { ChunkEntry } from './types'

export default function App() {
  const { manifest, error } = useManifest()
  const [selected, setSelected] = useState<ChunkEntry | null>(null)

  if (error) return (
    <div style={{ padding: 40, color: '#c00', fontFamily: 'monospace' }}>
      Manifest non trovato.<br />
      Esegui prima: <code>python pipeline/run_all.py</code>
      <br /><small>{error}</small>
    </div>
  )

  if (!manifest) return (
    <div style={{ padding: 40, color: '#999', fontFamily: 'sans-serif' }}>
      Caricamento…
    </div>
  )

  return (
    <div style={{ display: 'flex', height: '100vh', fontFamily: 'system-ui, sans-serif', background: '#f5f5f2' }}>
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', padding: 24, gap: 12 }}>
        <div style={{ fontSize: 11, color: '#999' }}>
          lociA · {manifest.snapshot_id} · {manifest.date} · {manifest.chunks.length} chunks
        </div>
        <MapViewer manifest={manifest} onSelect={setSelected} selected={selected} />
      </div>
      <div style={{
        width: 320, borderLeft: '1px solid #e0e0dc', background: '#fff',
        display: 'flex', flexDirection: 'column',
      }}>
        <div style={{ padding: '14px 20px', borderBottom: '1px solid #eee', fontSize: 12, fontWeight: 600, color: '#555' }}>
          Chunk
        </div>
        <ChunkPanel chunk={selected} />
      </div>
    </div>
  )
}

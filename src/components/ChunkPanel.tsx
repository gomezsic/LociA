import type { ChunkEntry } from '../types'

interface Props {
  chunk: ChunkEntry | null
}

export function ChunkPanel({ chunk }: Props) {
  if (!chunk) {
    return (
      <div style={{ padding: 24, color: '#aaa', fontSize: 13 }}>
        Clicca un punto sulla mappa per leggere il chunk.
      </div>
    )
  }

  return (
    <div style={{ padding: 20, fontSize: 13, lineHeight: 1.6 }}>
      <div style={{ fontSize: 10, color: '#aaa', marginBottom: 6 }}>
        {chunk.source_file}
      </div>
      <div style={{ fontSize: 11, color: '#888', marginBottom: 10 }}>
        {chunk.heading_path.join(' › ')}
      </div>
      <div style={{
        background: '#f5f5f0', borderRadius: 4, padding: '10px 12px',
        fontSize: 12, color: '#333', whiteSpace: 'pre-wrap', maxHeight: 400, overflowY: 'auto',
      }}>
        {chunk.text_preview}
        {chunk.text_preview.length >= 200 && <span style={{ color: '#bbb' }}> …</span>}
      </div>
      <div style={{ marginTop: 10, fontSize: 10, color: '#bbb' }}>
        cluster {chunk.cluster_id} · {chunk.chunk_id}
      </div>
    </div>
  )
}

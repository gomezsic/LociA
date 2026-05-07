import { useRef, useEffect, useState } from 'react'
import type { ChunkEntry, Manifest } from '../types'

interface Props {
  manifest: Manifest
  onSelect: (chunk: ChunkEntry) => void
  selected: ChunkEntry | null
}

const W = 800
const H = 600
const PAD = 40

function clusterColor(id: number, total: number): string {
  const hue = Math.round((id / Math.max(total, 1)) * 360)
  return `hsl(${hue}, 65%, 55%)`
}

export function MapViewer({ manifest, onSelect, selected }: Props) {
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const [hovered, setHovered] = useState<ChunkEntry | null>(null)
  const [tooltip, setTooltip] = useState<{ x: number; y: number } | null>(null)

  const nClusters = Math.max(...manifest.chunks.map(c => c.cluster_id)) + 1

  function toCanvas(coords: [number, number]): [number, number] {
    return [
      PAD + coords[0] * (W - PAD * 2),
      PAD + (1 - coords[1]) * (H - PAD * 2),
    ]
  }

  function chunkAt(mx: number, my: number): ChunkEntry | null {
    for (const c of manifest.chunks) {
      const [cx, cy] = toCanvas(c.coords)
      if (Math.hypot(mx - cx, my - cy) < 10) return c
    }
    return null
  }

  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return
    const ctx = canvas.getContext('2d')!

    ctx.clearRect(0, 0, W, H)
    ctx.fillStyle = '#fafaf8'
    ctx.fillRect(0, 0, W, H)

    // Grid
    ctx.strokeStyle = '#e8e8e4'
    ctx.lineWidth = 0.5
    for (let x = PAD; x <= W - PAD; x += (W - PAD * 2) / 10) {
      ctx.beginPath(); ctx.moveTo(x, PAD); ctx.lineTo(x, H - PAD); ctx.stroke()
    }
    for (let y = PAD; y <= H - PAD; y += (H - PAD * 2) / 8) {
      ctx.beginPath(); ctx.moveTo(PAD, y); ctx.lineTo(W - PAD, y); ctx.stroke()
    }

    // Points
    for (const c of manifest.chunks) {
      const [x, y] = toCanvas(c.coords)
      const isSelected = selected?.chunk_id === c.chunk_id
      const isHovered = hovered?.chunk_id === c.chunk_id
      const color = clusterColor(c.cluster_id, nClusters)

      ctx.beginPath()
      ctx.arc(x, y, isSelected ? 9 : isHovered ? 8 : 6, 0, Math.PI * 2)
      ctx.fillStyle = color
      ctx.globalAlpha = isSelected ? 1 : 0.82
      ctx.fill()
      ctx.globalAlpha = 1
      ctx.strokeStyle = isSelected ? '#222' : 'white'
      ctx.lineWidth = isSelected ? 2 : 1
      ctx.stroke()
    }
  }, [manifest, selected, hovered, nClusters])

  function handleMouseMove(e: React.MouseEvent<HTMLCanvasElement>) {
    const rect = (e.target as HTMLCanvasElement).getBoundingClientRect()
    const mx = e.clientX - rect.left
    const my = e.clientY - rect.top
    const found = chunkAt(mx, my)
    setHovered(found)
    setTooltip(found ? { x: e.clientX - rect.left + 12, y: e.clientY - rect.top - 8 } : null)
  }

  function handleClick(e: React.MouseEvent<HTMLCanvasElement>) {
    const rect = (e.target as HTMLCanvasElement).getBoundingClientRect()
    const found = chunkAt(e.clientX - rect.left, e.clientY - rect.top)
    if (found) onSelect(found)
  }

  return (
    <div style={{ position: 'relative', display: 'inline-block' }}>
      <canvas
        ref={canvasRef}
        width={W}
        height={H}
        style={{ cursor: hovered ? 'pointer' : 'default', border: '1px solid #e0e0dc', borderRadius: 6 }}
        onMouseMove={handleMouseMove}
        onMouseLeave={() => { setHovered(null); setTooltip(null) }}
        onClick={handleClick}
      />
      {hovered && tooltip && (
        <div style={{
          position: 'absolute', left: tooltip.x, top: tooltip.y,
          background: 'rgba(30,30,26,0.88)', color: '#fff', fontSize: 11,
          padding: '4px 8px', borderRadius: 4, pointerEvents: 'none',
          maxWidth: 240, whiteSpace: 'pre-wrap', zIndex: 10,
        }}>
          {hovered.heading_path.join(' › ')}
        </div>
      )}
    </div>
  )
}

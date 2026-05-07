export interface ChunkEntry {
  chunk_id: string
  coords: [number, number]
  cluster_id: number
  source_file: string
  heading_path: string[]
  text_preview: string
}

export interface Manifest {
  lociA_version: string
  snapshot_id: string
  date: string
  origin_image: string
  snapshot_image: string
  codec: {
    color_scheme: string
    layout_strategy: string
  }
  chunks: ChunkEntry[]
}

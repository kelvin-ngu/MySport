import { Injectable } from '@angular/core';
import { PostDetail } from './postdetail';

@Injectable({
  providedIn: 'root'
})
export class PostgatheringService {
  postDetail!: PostDetail;
  constructor() {
  }
  url = 'http://localhost:3000/getposts';

  async getPost(): Promise<PostDetail> {
    const data = await fetch(this.url);
    return await data.json() ?? [];
  }

}

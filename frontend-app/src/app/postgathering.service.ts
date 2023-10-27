import { Injectable, inject } from '@angular/core';
import { PostDetail } from './postdetail';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class PostgatheringService {
  postDetail!: PostDetail;
  httpClient: HttpClient  = inject(HttpClient);
  url = 'http://localhost:8000/forum/post/5153ce07-5576-4871-ad75-6578ba537a07/';
  constructor() {
  }
  getPost() {
    return this.httpClient.get(this.url);
  }
}

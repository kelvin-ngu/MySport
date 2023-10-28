import { Injectable, inject } from '@angular/core';
import { PostDetail } from './postdetail';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class GetFormService {
  postDetail!: PostDetail;
  httpClient: HttpClient  = inject(HttpClient);
  url = 'http://localhost:8000/journal/';
  constructor() {
  }
  getForms() {
    return this.httpClient.get(this.url);
  }
}
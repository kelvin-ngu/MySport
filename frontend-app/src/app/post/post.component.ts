import { Component, Input } from '@angular/core';
import { PostDetail } from '../postdetail';

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.css'],
  standalone: true
})
export class PostComponent {
  @Input() postDetail!: PostDetail;


  
}

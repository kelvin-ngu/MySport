import { Component, Input } from '@angular/core';
import { Postlist } from '../postlist';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.css'],
  imports: [CommonModule],
  standalone: true
})
export class PostComponent {
  @Input() postList!: Postlist;  
}

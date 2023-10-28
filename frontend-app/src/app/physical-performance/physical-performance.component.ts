import { Component, Input } from '@angular/core';
import { Postlist } from '../postlist';
import { PostComponent } from '../post/post.component';

@Component({
  selector: 'app-physical-performance',
  templateUrl: './physical-performance.component.html',
  styleUrls: ['./physical-performance.component.css'],
  imports: [PostComponent],
  standalone: true
})
export class PhysicalPerformanceComponent {
  @Input() postList!: Postlist;  
}

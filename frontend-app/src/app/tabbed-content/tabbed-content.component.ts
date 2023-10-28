// tabbed-content.component.ts
import { Component, inject } from '@angular/core';
import { PhysicalCareComponent } from '../physical-care/physical-care.component';
import { PhysicalPerformanceComponent } from '../physical-performance/physical-performance.component';
import { PlayerVoiceComponent } from '../player-voice/player-voice.component';
import { MentalHealthComponent } from '../mental-health/mental-health.component';
import { CommonModule } from '@angular/common';
import { PostgatheringService } from '../postgathering.service';
import { Postlist } from '../postlist';

@Component({
  selector: 'app-tabbed-content',
  templateUrl: './tabbed-content.component.html',
  styleUrls: ['./tabbed-content.component.css'],
  imports: [PhysicalCareComponent,
    PhysicalPerformanceComponent,
    PlayerVoiceComponent,
    MentalHealthComponent,
    CommonModule],
  standalone: true
})

export class TabbedContentComponent {
  postgatheringService: PostgatheringService  = inject(PostgatheringService);
  postList!: Postlist;
  selectedTab: string = ''; // Initialize as an empty string
  selectTab(tab: string): void {
    this.selectedTab = tab;
  }
  constructor(){
    this.postgatheringService.getPost().subscribe((response) => {
      const jsonString = JSON.stringify(response);
      this.postList = JSON.parse(jsonString);
    });

  }
}
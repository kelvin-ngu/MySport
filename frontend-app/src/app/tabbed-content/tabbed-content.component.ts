// tabbed-content.component.ts
import { Component } from '@angular/core';
import { PhysicalCareComponent } from '../physical-care/physical-care.component';
import { PhysicalPerformanceComponent } from '../physical-performance/physical-performance.component';
import { PlayerVoiceComponent } from '../player-voice/player-voice.component';
import { MentalHealthComponent } from '../mental-health/mental-health.component';

@Component({
  selector: 'app-tabbed-content',
  templateUrl: './tabbed-content.component.html',
  styleUrls: ['./tabbed-content.component.css'],
  imports: [PhysicalCareComponent,
    PhysicalPerformanceComponent,
    PlayerVoiceComponent,
    MentalHealthComponent],
  standalone: true
})
export class TabbedContentComponent {
  selectedTab: string = ''; // Initialize as an empty string
  selectTab(tab: string): void {
    this.selectedTab = tab;
  }
}